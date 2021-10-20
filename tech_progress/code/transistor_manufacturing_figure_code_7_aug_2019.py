# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:42:41 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_wafer_cost = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Transistors/Kurzweil_2005_wafer_cost.csv")


marker_size = 5
fig = plt.figure()
plt.yscale("log")
plt.scatter(df_wafer_cost.index, df_wafer_cost["1 micron"], label = "1 micron", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.7 microns"], label = "0.7 microns", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.5 microns"], label = "0.5 microns", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.35 microns"], label = "0.35 microns", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.25 microns"], label = "0.25 microns", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.18 microns"], label = "0.18 microns", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.13 microns"], label = "0.13 microns", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.09 microns"], label = "0.09 microns", marker = "x")
plt.scatter(df_wafer_cost.index, df_wafer_cost["0.065 microns"], label = "0.065 microns", marker = "x")


plt.ylabel('Wafer costs per transistor (US $)')
plt.xlabel('Year')
plt.legend(markerscale = 1, prop={'size': 9})
plt.title("Transistor Manufacturing Costs over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/transistor_manufacturing_progress.pdf")
