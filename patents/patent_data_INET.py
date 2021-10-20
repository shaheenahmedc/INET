# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:26:41 2019

@author: Shaheen
"""
import pandas as pd
#from enchant.tokenize import get_tokenizer
#import enchant
from nltk.corpus import brown
#import nltk
#nltk.download('brown')

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

def read_first_n_rows(filename, n):
    df = pd.read_csv(filename, index_col = 0, nrows = n)
    return df

def read_large_file_x_patents(filename, n):
    iter_csv = pd.read_csv(filename, iterator = True, chunksize = n, index_col = 0)
    df = pd.concat([chunk[chunk.index.str.startswith('X')] for chunk in iter_csv])
    return df

def read_large_file(filename, n):
    iter_csv = pd.read_csv(filename, iterator = True, chunksize = n, index_col = 0)
    df = pd.concat([chunk for chunk in iter_csv])
    return df

def add_spelling_mistake_bool(dataframe, name_of_column_with_text):
    dataframe[name_of_column_with_text] = dataframe[name_of_column_with_text].astype(str)
    dataframe['Spelling mistake'] = ""
    word_list = brown.words()
    word_set = set(word_list)
    print (word_set)
    for index, row in dataframe.iterrows():
        i = row[name_of_column_with_text]
        correct_bool = True
        i_tokenised = i.split()
        for k in i_tokenised:
            if (k in word_set):
                continue
            else:
                correct_bool = False
        if correct_bool == False:
            print (index)
            dataframe.set_value(index, 'Spelling mistake', True)
    return dataframe
            
        
        
#df = read_data("F:/Files - INET - Summer 2019/mcfpat1804_X_patent_numbers.txt")
#df_sample = df.sample(n = 50)
#df_sample.to_csv("F:/Files - INET - Summer 2019/mcfpat1804_X_patent_numbers_random_50.txt", sep='\t')
#df_first_n_rows = read_first_n_rows("F:/Files - INET - Summer 2019/mcfpat1804.txt", 1000)

df_google_pats = read_first_n_rows("F:/Files - INET - Summer 2019/GooglePats.csv", 10000)

df_google_pats = add_spelling_mistake_bool(df_google_pats, 'text')
        
df_google_pats = df_google_pats[df_google_pats['Spelling mistake'] == True]