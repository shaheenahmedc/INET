# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:35:16 2019

@author: Shaheen
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, index_col = 0, skipfooter = 1, engine = 'python')
    return df

df_funk_lifetimes = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/quantum_computation/Funk2015_lifetimes.csv")
df_funk_qubits = read_data("F:/Files - INET - Summer 2019/Shaheen_tech_progress_data/quantum_computation/Funk2015_bits.csv")


marker_size = 5
fig, ax1 = plt.subplots()
ax1.set_yscale("log")
ax1.plot(df_funk_lifetimes.index, df_funk_lifetimes["Relaxation time"], label = "Relaxation time", marker = 'x')
ax1.plot(df_funk_lifetimes.index, df_funk_lifetimes["Coherence time"], label = "Coherence time", marker = 'x')

ax2 = ax1.twinx()
ax2.set_yscale("log")

ax2.plot(df_funk_qubits.index, df_funk_qubits["Number of qubits"], label = "Number of qubits", marker = 'x', color = 'r')

ax1.set_ylabel('Time(seconds)')
ax2.set_ylabel('Number of Qubits')

plt.xlabel('Year')
ax1.legend(markerscale = 1, prop={'size': 7}, loc = 0)
ax2.legend(markerscale = 1, prop={'size': 7}, loc = 4)

plt.title("Typical Lifetimes and Numbers of Qubits in QC over Time")
plt.savefig("F:/Files - INET - Summer 2019/Figures/Final_report/quantum_computers_progress.pdf")
