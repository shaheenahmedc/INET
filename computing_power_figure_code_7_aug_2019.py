# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:17:57 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Microprocessors/Chang_2010_computer_power.csv")
df_manual = df[df["Technology"] == 'Manual']
df_mechanical = df[df["Technology"] == 'Mechanical']
df_relay = df[df["Technology"] == 'Relay/Vacuum']
df_transistors = df[df["Technology"] == 'Transistors']
df_microprocessors = df[df["Technology"] == 'Microprocessors']


marker_size = 10
fig = plt.figure()
plt.yscale("log")
plt.scatter(df_manual.index, df_manual["Computer Power(MSOPS)"], label = "Manual", s = marker_size)
plt.scatter(df_mechanical.index, df_mechanical["Computer Power(MSOPS)"], label = "Mechanical", s = marker_size)
plt.scatter(df_relay.index, df_relay["Computer Power(MSOPS)"], label = "Relay/Vacuum", s = marker_size)
plt.scatter(df_transistors.index, df_transistors["Computer Power(MSOPS)"], label = "Transistors", s = marker_size)
plt.scatter(df_microprocessors.index, df_microprocessors["Computer Power(MSOPS)"], label = "Microprocessors", s = marker_size)


plt.ylabel('Million Standardized Operations per Second')
plt.xlabel('Year')
plt.legend(markerscale = 3)
plt.title("Computing Power over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/computing_power_progress.pdf")