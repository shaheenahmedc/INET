# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:04:05 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_microprocessor = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Microprocessors/Kurzweil_2005_microprocessor_clock_speed.csv")

marker_size = 5
fig = plt.figure()
plt.yscale("log")
plt.scatter(df_microprocessor.index, df_microprocessor["Hz"], label = "21")

plt.ylabel('Hz')
plt.xlabel('Year')
plt.legend(markerscale = 1)
plt.title("Microprocessor Clock Speed")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/microprocessor_clock_speed_progress.pdf")
