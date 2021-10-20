# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:35:42 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt
def read_data(filename):
    df = pd.read_csv(filename, index_col = 0, skipfooter = 1, engine = 'python')
    return df

df_bishop_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Bishop2017_Sequencing.csv")
df_bishop_synth = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Bishop2017_Synthesis.csv")
df_brogg_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Broggiato_2014_sequencing.csv")
df_kurz_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Kurzweil_2005_DNA_sequencing_per_base_pair.csv")
df_nas_ss = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/NAS_2017_ssDNA.csv")
df_nas_ds = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/NAS_2017_dsDNA.csv")
df_nas_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/NAS_2017_Sequencing.csv")
df_shend = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Shendure2004_polonies.csv")
df_pcdb_cap = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Capillary_DNA_Sequencing_PCDB.csv")
df_pcdb_shot = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Shotgun_Sanger_DNA_Sequencing_PCDB.csv")


marker_size = 5
fig = plt.figure()
plt.yscale("log")
plt.plot(df_bishop_seq.index, df_bishop_seq["Sequencing Cost ($ per base pair)"], label = "Bishop 2017 Sequencing", marker = 'x')
plt.plot(df_brogg_seq.index, df_brogg_seq["Sequencing Cost ($ per base pair)"], label = "Broggiato 2014 Sequencing", marker = 'x')
plt.plot(df_kurz_seq.index, df_kurz_seq["Cost ($ per base pair)"], label = "Kurzweil 2005 Sequencing", marker = 'x')
plt.plot(df_nas_seq.index, df_nas_seq["DNA Sequencing ($ per base pair)"], label = "NAS 2017 Sequencing", marker = 'x')
plt.plot(df_shend.index, df_shend["Polonies Sequencing ($ per base pair)"], label = "Shendure 2004 Polonies Sequencing", marker = 'x')
plt.plot(df_pcdb_cap.index, df_pcdb_cap["Cost (USD/Base Pair)"], label = "PCDB Capillary Seqencing", marker = 'x')
plt.plot(df_pcdb_shot.index, df_pcdb_shot["Cost (USD/Base Pair)"], label = "PCDB SS Seqencing", marker = 'x')

plt.ylabel('US $/Base Pair')
plt.xlabel('Year')
plt.legend(markerscale = 1, prop={'size': 7})
plt.title("Cost per Base Pair Sequencing over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Final_report/Seq_progress.pdf")

