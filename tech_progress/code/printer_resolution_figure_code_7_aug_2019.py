# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:59:48 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0)
    return df

df_dot = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Printers/Sood_2005_dot_matrix_$_kdpi.csv")
df_ink = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Printers/Sood_2005_inkjet_$_kdpi.csv")
df_laser = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Printers/Sood_2005_laser_$_kdpi.csv")
df_thermal = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/hardware/Printers/Sood_2005_thermal_$_kdpi.csv")



marker_size = 20
fig = plt.figure()
plt.yscale("log")
plt.plot(df_dot.index, df_dot["US $/Kdpi_sqr"], label = "23")
plt.plot(df_ink.index, df_ink["US $/Kdpi_sqr"], label = "24")
plt.plot(df_laser.index, df_laser["US $/Kdpi_sqr"], label = "25")
plt.plot(df_thermal.index, df_thermal["US $/Kdpi_sqr"], label = "26")


plt.ylabel('US $/kdpi_sqr')
plt.xlabel('Year')
plt.legend(markerscale = 3)
plt.title("Printer Resolution over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Progress_report/printer_resolution_progress.pdf")
