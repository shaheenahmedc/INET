# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:32:07 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0, skipfooter = 1, engine = 'python')
    return df

#df_bishop_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Bishop2017_Sequencing.csv")
df_bishop_synth = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Bishop2017_Synthesis.csv")
#df_brogg_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Broggiato_2014_sequencing.csv")
#df_kurz_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Kurzweil_2005_DNA_sequencing_per_base_pair.csv")
df_nas_ss = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/NAS_2017_ssDNA.csv")
df_nas_ds = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/NAS_2017_dsDNA.csv")
#df_nas_seq = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/NAS_2017_Sequencing.csv")
#df_shend = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Shendure2004_polonies.csv")
#df_pcdb_cap = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Capillary_DNA_Sequencing_PCDB.csv")
#df_pcdb_shot = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/genomics/DNA_Sequencing/Shotgun_Sanger_DNA_Sequencing_PCDB.csv")


marker_size = 5
fig = plt.figure()
plt.yscale("log")
#plt.plot(df_bishop_seq.index, df_bishop_seq["Sequencing Cost ($ per base pair)"], label = "Bishop 2017 Sequencing", marker = 'x')
plt.plot(df_bishop_synth.index, df_bishop_synth["Synthesis Cost ($ per base pair)"], label = "Bishop 2017 Synthesis", marker = 'x')
#plt.plot(df_brogg_seq.index, df_brogg_seq["Sequencing Cost ($ per base pair)"], label = "Broggiato 2014 Sequencing", marker = 'x')
#plt.plot(df_kurz_seq.index, df_kurz_seq["Cost ($ per base pair)"], label = "Kurzweil 2005 Sequencing", marker = 'x')
plt.plot(df_nas_ss.index, df_nas_ss["ssDNA Synthesis Cost ($ per base pair)"], label = "NAS 2017 ssDNA Synthesis", marker = 'x')
plt.plot(df_nas_ds.index, df_nas_ds["dsDNA Synthesis Cost ($ per base pair)"], label = "NAS 2017 dsDNA Synthesis", marker = 'x')
#plt.plot(df_nas_seq.index, df_nas_seq["DNA Sequencing ($ per base pair)"], label = "NAS 2017 Sequencing", marker = 'x')
#plt.plot(df_shend.index, df_shend["Polonies Sequencing ($ per base pair)"], label = "Shendure 2004 Polonies Sequencing", marker = 'x')
#plt.plot(df_pcdb_cap.index, df_pcdb_cap["Cost (USD/Base Pair)"], label = "PCDB Capillary Seqencing", marker = 'x')
#plt.plot(df_pcdb_shot.index, df_pcdb_shot["Cost (USD/Base Pair)"], label = "PCDB SS Seqencing", marker = 'x')


#df_jcmit_disk_drives_slope, df_jcmit_disk_drives_intercept, df_jcmit_disk_drives_r_value, df_jcmit_disk_drives_p_value, df_jcmit_disk_drives_std_err = stats.linregress(df_jcmit_disk_drives.index, np.log(df_jcmit_disk_drives["US $/Megabyte"]))
#print (np.log(df_jcmit_disk_drives["US $/Megabyte"]))
#print (df_jcmit_disk_drives_slope)
#print (df_jcmit_disk_drives_intercept)
#plt.plot(df_jcmit_disk_drives.index, df_jcmit_disk_drives_intercept + df_jcmit_disk_drives_slope*df_jcmit_disk_drives.index, 'r', label='fitted line')
#y_fit = np.exp(df_jcmit_disk_drives_slope*df_jcmit_disk_drives.index + df_jcmit_disk_drives_intercept)
#plt.plot(df_jcmit_disk_drives.index, y_fit)

plt.ylabel('US $/Base Pair')
plt.xlabel('Year')
plt.legend(markerscale = 1, prop={'size': 7})
plt.title("Cost per Base Pair Synthesis over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Final_report/Synth_progress.pdf")
