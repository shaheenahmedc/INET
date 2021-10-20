# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:11:24 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_microprocessor = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Microprocessors/Kurzweil_2005_microprocessor_cost_per_cycle.csv")

marker_size = 5
fig = plt.figure()
plt.yscale("log")
plt.scatter(df_microprocessor.index, df_microprocessor["$/Transistor/Hz"], label = "21", marker = "x")

plt.ylabel('$/Transistor/Hz')
plt.xlabel('Year')
plt.legend(markerscale = 1)
plt.title("Microprocessor Cost per Transistor Cycle")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/microprocessor_cost_per_cycle_progress.pdf")