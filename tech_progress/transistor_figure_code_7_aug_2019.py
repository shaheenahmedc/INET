# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:05:15 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_kurzweil_2005_transistor = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Transistors/Kurzweil_2005_transistor_price.csv")
df_transistor_pcdb = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Transistors/Transistor_PCDB.csv")


marker_size = 5
fig = plt.figure()
plt.yscale("log")
plt.scatter(df_kurzweil_2005_transistor.index, df_kurzweil_2005_transistor["Average Transistor Price"], label = "19")
plt.scatter(df_transistor_pcdb.index, df_transistor_pcdb["Average Transistor Price"], label = "PCDB")


plt.ylabel('Average Transistor Price (1968 Price = 1)')
plt.xlabel('Year')
plt.legend(markerscale = 2)
plt.title("Cost of Transistors over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/transistor_progress.pdf")