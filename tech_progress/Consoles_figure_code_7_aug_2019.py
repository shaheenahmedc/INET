# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:18:55 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_consoles = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Games_consoles/Consoles_CPU_Score.csv")

marker_size = 20
fig = plt.figure()
plt.yscale("log")
plt.scatter(df_consoles.index, df_consoles["CPU Score"], label = "27")

plt.ylabel('CPU Score')
plt.xlabel('Year')
plt.legend(markerscale = 2)
plt.title("Console CPU Score over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/Consoles_progress.pdf")