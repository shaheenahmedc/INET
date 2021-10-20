# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:59:21 2019

@author: Shaheen
"""

import pandas as pd
import nltk 
import numpy as np
nltk.download("words")
nltk.download("stopwords")
nltk.download("brown")
nltk.download("wordnet")
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from spellchecker import SpellChecker
from pathlib import Path
import matplotlib.pyplot as plt

'''
This function reads in n rows from a given csv file
'''
def read_first_n_rows(filename, n):
    df = pd.read_csv(filename, index_col = 0, nrows = n)
    return df

'''
This function checks which entries in a column of text has spelling mistakes. 
It takes a dataframe containing the patent data, the name of the column with text to check, 
and a 'round of checking' as input. 
'round of checking' = 1 for checking original text
'round of checking' = 2 for checking corrected text for improvement. See document for more details. 
'''
def add_spelling_mistake_bool(dataframe, name_of_column_with_text, round_of_checking):
    Lem = WordNetLemmatizer()
    dataframe[name_of_column_with_text] = dataframe[name_of_column_with_text].astype(str)
    dataframe[name_of_column_with_text] = dataframe[name_of_column_with_text].str.lower()
    dataframe[name_of_column_with_text] = dataframe[name_of_column_with_text].str.replace(r"[^a-zA-Z]+", " ")
    word_list = words.words()
    word_set = set(word_list)
    stopword_list = stopwords.words()
    stopword_set = set(stopword_list)
    brown_list = brown.words()
    brown_set = set(brown_list)   
    word_set = word_set|stopword_set
    word_set = word_set|brown_set  
    for index, row in dataframe.iterrows():
        i = row[name_of_column_with_text]
        mistake_bool = False
        i_tokenised = i.split()
        for k in i_tokenised:
            if (Lem.lemmatize(k, 'n') in word_set or Lem.lemmatize(k, 'v') in word_set):
                continue
            else:
                mistake_bool = True
                break
        if mistake_bool == True:
            dataframe.set_value(index, 'Spelling mistake - Round ' + str(round_of_checking), True)
        else:
            dataframe.set_value(index, 'Spelling mistake - Round ' + str(round_of_checking), False)
    return dataframe

'''
This function corrects spelling mistakes for a column of text, 
where a spelling mistake boolean column has already been generated. 
Edit_distance = amount of characters allowed to vary in spelling correction.
'''
def correct_spelling(dataframe, name_of_column_with_text, edit_distance):
    spell = SpellChecker(distance = edit_distance)
    for index, row in dataframe.iterrows():
        if row['Spelling mistake - Round 1'] == True:
            i = row[name_of_column_with_text]
            i_tokenised = i.split()
            print (index)
            for j,k in enumerate(i_tokenised):
                i_tokenised[j] = spell.correction(k)         
            i_tokenised_and_joined = " ".join(i_tokenised) 
            dataframe.set_value(index, 'Corrected spelling', i_tokenised_and_joined)
            if dataframe.loc[index, 'text'] != dataframe.loc[index, 'Corrected spelling']:
                dataframe.set_value(index, 'Has spelling been corrected?', True)
            else:
                dataframe.set_value(index, 'Has spelling been corrected?', False)
        else:
             dataframe.set_value(index, 'Has spelling been corrected?', False)
             dataframe.set_value(index, 'Corrected spelling', row[name_of_column_with_text])

    return dataframe

'''
This function runs the above functions, and stores the results
in two files, in the same parent directory as the file that is input.
It takes a filename, a number of rows to analyse, and an edit_distance as inputs. 
Encapsulated in run_process() below.
'''
def run_error_detection_and_correction(filename, number_of_rows, edit_distance):
    df = read_first_n_rows(filename, number_of_rows)
    df = add_spelling_mistake_bool(df, 'text', 1)    
    df = correct_spelling(df, 'text', edit_distance)              
    df = add_spelling_mistake_bool(df, 'Corrected spelling', 2)    
    parent_path = Path(filename).parent
    print (parent_path)
    patent_analysis_file_path = parent_path / "patent_analysis.xlsx"
    print (patent_analysis_file_path)
    df.to_excel(patent_analysis_file_path)
    print (df.dtypes)
    erroneous_rows_file_path = parent_path / "erroneous_rows.csv"
    df_erroneous_rows = df[df['Spelling mistake - Round 2'] == True]
    df_erroneous_rows.to_csv(erroneous_rows_file_path)
    
    return df

'''
This function extracts relevant performance statistics post error detection and correction completion. 
It takes a dataframe as input. 
Note that the row names used are added to the dataframe in the preceding process. 
'''
def extract_statistics(df):
    df['Year'] = df['publication_date'].astype(str).str[:-4].astype(np.int64) 
    group_by = df.groupby("Year")
    group_by_size = df.groupby("Year").size()
    new_df = pd.DataFrame(index = group_by_size.index)
    new_df["Total for year"] = group_by.size() 
    new_df["Total incorrect rows pre correction"] = group_by['Spelling mistake' + ' - ' + 'Round 1'].sum()
    new_df["Total correct rows pre correction"] = new_df["Total for year"] - new_df["Total incorrect rows pre correction"]
    new_df["Percentage incorrect pre correction"] = (new_df["Total incorrect rows pre correction"] / new_df["Total for year"] ) 
    new_df["Percentage correct pre correction"] = (new_df["Total correct rows pre correction"] / new_df["Total for year"] )  
    new_df["Total incorrect rows post correction"] = group_by['Spelling mistake' + ' - ' + 'Round 2'].sum()
    new_df["Total correct rows post correction"] = new_df["Total for year"] - new_df["Total incorrect rows post correction"]
    new_df["Percentage incorrect post correction"] = (new_df["Total incorrect rows post correction"] / new_df["Total for year"] ) 
    new_df["Percentage correct post correction"] = (new_df["Total correct rows post correction"] / new_df["Total for year"] ) 
    new_df["Percentage improvement"] = 1 - (new_df["Percentage incorrect post correction"] / new_df["Percentage incorrect pre correction"]) 
    return new_df

'''
This function visualises our results.
User can choose between percentage statistics or total statistics
via the percentage_bool variable. 
It is passed to the encapsulating run_process() function below. 
'''
def plot_results(df, percentage_bool, figure_folder):
    
    plt.figure()
    if percentage_bool == True:       
        plt.plot(df.index, df["Percentage incorrect pre correction"], label = "Incorrect pre-correction")
        plt.plot(df.index, df["Percentage incorrect post correction"], label = "Incorrect post-correction")
        plt.plot(df.index, df["Percentage improvement"], label = "Percentage improvement")
        plt.ylabel('Percentage of rows')
        plt.xlabel('Year')
        plt.legend(markerscale = 3)
        plt.title("Reduction in Spelling Mistakes of Patent Data")
        figure_path = figure_folder / "Percentage_reduction_in_mistakes.pdf"
        plt.savefig(figure_path)
    else:   
        plt.plot(df.index, df["Total incorrect rows pre correction"], label = "Incorrect pre-correction")
        plt.plot(df.index, df["Total incorrect rows post correction"], label = "Incorrect post-correction")
        plt.plot(df.index, df["Total for year"], label = "Total rows for year")
        plt.ylabel('Number of Rows')
        plt.xlabel('Year')
        plt.legend(markerscale = 3)
        plt.title("Reduction in Spelling Mistakes of Patent Data")
        figure_path = figure_folder / "Total_reduction_in_mistakes.pdf"
        plt.savefig(figure_path)
  
'''
This function encapsulates all of the above function, and 
is the only function the user is required to run. 
It takes a filename, a number of rows, an edit_distance and a 
percentage_bool as variables. 
The use of the pathlib library should account for differences in 
file path notation across Mac and Windows OS', but the user should be aware of 
potential issues nevertheless. 
False percentage_bool = total statistics. 
True percentage bool = percentage statistics. 
'''
def run_process(filename, number_of_rows, edit_distance, percentage_bool):
    df = run_error_detection_and_correction(filename, number_of_rows, edit_distance)    
    df_statistics = extract_statistics(df)   
    parent_path = Path(filename).parent
    plot_results(df_statistics, percentage_bool, parent_path)
    
'''
This function can test if a word is in the wordset used in add_spelling_mistake_bool.
Outputs boolean indicating if word in wordset, as well as noun and verb-lemmatized forms of the word. 
'''
def test_word(text):
    word_list = words.words()
    word_set = set(word_list)
    stopword_list = stopwords.words()
    stopword_set = set(stopword_list)
    brown_list = brown.words()
    brown_set = set(brown_list)   
    wordnet_list = wordnet.words()
    wordnet_set = set(wordnet_list) 
    word_set = word_set|stopword_set
    word_set = word_set|brown_set  
    word_set = word_set | wordnet_set
    
    Lem = WordNetLemmatizer()
    if (Lem.lemmatize(text, 'n') in word_set or Lem.lemmatize(text, 'v') in word_set):
        print (True, Lem.lemmatize(text, 'n'), Lem.lemmatize(text, 'v'))
    else:
        print (False, Lem.lemmatize(text, 'n'), Lem.lemmatize(text, 'v'))
  
#Examples of running run_process() and test_word()
#run_process("F:/Files - INET - Summer 2019/Patent Work/GooglePats.csv", 100, 1, True)      
test_word('lubricating')
        
