# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:10:39 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_kurzweil_2005_ram = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Kurzweil_2005_ram_cleaned.csv")

df_victor_2002_4K = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_4K_cleaned.csv")

df_victor_2002_16K = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_16K_cleaned.csv")

df_victor_2002_64K = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_64K_cleaned.csv")

df_victor_2002_256K = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_256K_cleaned.csv")

df_victor_2002_1M = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_1M_cleaned.csv")

df_victor_2002_4M = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_4M_cleaned.csv")

df_victor_2002_16M = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_16M_cleaned.csv")

df_victor_2002_64M = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/Victor_2002_64M_cleaned.csv")

df_dram_pcdb = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/RAM/DRAM_PCDB.csv")


marker_size = 5
fig = plt.figure()
plt.yscale("log")
plt.plot(df_kurzweil_2005_ram.index, df_kurzweil_2005_ram["US $/Megabit"], label = "10")
plt.plot(df_victor_2002_4K.index, df_victor_2002_4K["US $/Megabit"], label = "11")
plt.plot(df_victor_2002_16K.index, df_victor_2002_16K["US $/Megabit"], label = "12")
plt.plot(df_victor_2002_64K.index, df_victor_2002_64K["US $/Megabit"], label = "13")
plt.plot(df_victor_2002_256K.index, df_victor_2002_256K["US $/Megabit"], label = "14")
plt.plot(df_victor_2002_1M.index, df_victor_2002_1M["US $/Megabit"], label = "15")
plt.plot(df_victor_2002_4M.index, df_victor_2002_4M["US $/Megabit"], label = "16")
plt.plot(df_victor_2002_16M.index, df_victor_2002_16M["US $/Megabit"], label = "17")
plt.plot(df_victor_2002_64M.index, df_victor_2002_64M["US $/Megabit"], label = "18")
plt.plot(df_dram_pcdb.index, df_dram_pcdb["US $/Megabit"], label = "PCDB", color = 'k')


plt.ylabel('US $/Megabit')
plt.xlabel('Year')
plt.legend(markerscale = 5)
plt.title("Cost per Megabit of RAM over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/RAM_progress.pdf")
