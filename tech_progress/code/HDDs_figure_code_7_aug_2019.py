# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:35:42 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_jcmit_disk_drives = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/JCMIT_disk_drives_cleaned.csv")
df_jcmit_flash = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/JCMIT_flash_cleaned.csv")
df_jcmit_ssds = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/JCMIT_SSDs_cleaned.csv")
df_jcmit_memory = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/JCMIT_memory_cleaned.csv")
df_kurzweil_2005 = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/Kurzweil_2005_magnetic_storage_cleaned.csv")
df_mkomo_hdds = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/Mkomo_HDDs_cleaned.csv")
df_sood_2005_magnetic = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/Sood_2005_desktop_memory_magnetic_cleaned.csv")
df_sood_2005_optical = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/Sood_2005_desktop_memory_optical_cleaned.csv")
df_sood_2005_magneto_optical = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/Sood_2005_desktop_memory_magneto_optical_cleaned.csv")
df_pcdb = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/HDDs/HDDs_PCDB.csv")

marker_size = 1
fig = plt.figure()
plt.yscale("log")
plt.scatter(df_jcmit_disk_drives.index, df_jcmit_disk_drives["US $/Megabyte"], s = marker_size, label = "1")
plt.scatter(df_jcmit_flash.index, df_jcmit_flash["US $/Megabyte"], s = marker_size, label = "2")
plt.scatter(df_jcmit_ssds.index, df_jcmit_ssds["US $/Megabyte"], s = marker_size, label = "3")
plt.scatter(df_jcmit_memory.index, df_jcmit_memory["US $/Megabyte"], s = marker_size, label = "4")
plt.scatter(df_kurzweil_2005.index, df_kurzweil_2005["US $/Megabyte"], s = marker_size, label = "5 (2000 US $)")
plt.scatter(df_mkomo_hdds.index, df_mkomo_hdds["US $/Megabyte"], s = marker_size, label = "6")
plt.scatter(df_sood_2005_magnetic.index, df_sood_2005_magnetic["US $/Megabyte"], s = marker_size, label = "7")
plt.scatter(df_sood_2005_magneto_optical.index, df_sood_2005_magneto_optical["US $/Megabyte"], s = marker_size, label = "8")
plt.scatter(df_sood_2005_optical.index, df_sood_2005_optical["US $/Megabyte"], s = marker_size, label = "9")
plt.plot(df_pcdb.index, df_pcdb["Price (2005 USD/Megabyte)"], label = "PCDB (2005 US $)", color = 'k')

plt.ylabel('US $/Megabyte')
plt.xlabel('Year')
plt.legend(markerscale = 5, prop={'size': 7})
plt.title("Cost per Megabyte of Data Storage over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/HDDs_progress.pdf")

