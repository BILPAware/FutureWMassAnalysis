#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:07:41 2024

@author: user288
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams["figure.autolayout"] = True
columns = ["W_mass", "Chi2"]
df = pd.read_csv("/home/user288/FutureWMassAnalysis/outputChi2_semilep_leptonic_channelMt.csv", usecols=columns)

x = df.W_mass
y = df.Chi2

def parabola(x, a, b, c):
    return a*x**2 + b*x + c

parameters, covariance = curve_fit(parabola, x, y)

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]


z = np.linspace(x[0], x[np.argmax(x)], 100)

fit_y = parabola(z, fit_A, fit_B, fit_C)

mw = - (fit_B)/(2*fit_A)

perr = np.sqrt(np.diag(covariance))

A_err = perr[0]
B_err = perr[1]
C_err = perr[2]

unc = (np.sqrt((B_err/(2*fit_A))**2+((fit_B*A_err)/(2*fit_A**2))**2))

print(unc)

print(parameters)
print(perr)

#print(covariance)

print(mw)

mw_up = mw + unc
mw_lo = mw - unc

plt.vlines(mw, 0, 60, 'k', '--')
#plt.vlines(mw_up, 0, 80, 'r', '--')
#plt.vlines(mw_lo, 0, 80, 'r', '--')

plt.plot(x, y, 'o', label='Data')
plt.plot(z, fit_y, '-', label='Fit')
plt.legend()