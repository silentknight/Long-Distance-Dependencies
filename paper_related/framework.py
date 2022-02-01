#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats

######################################################################################################################
with plt.style.context(('seaborn')):

    x = np.linspace(1, 10000, 10000)

    ##########################################################################################################################

    #break_point = 5
    #alpha_1 = 0.4
    #alpha_2 = 0.05
    #amplitude = 1.2
    #f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    #fit_sample = f(x)
    #p1 = plt.loglog(x, fit_sample, label="Broken Power-Law Decay")

    ##########################################################################################################################

    #a = 2
    #alpha = 0.1
    #y = a*pow(x,-alpha)
    #p2 = plt.loglog(x, y, label="Power-Law Decay")

    ##########################################################################################################################

    # a = 1
    # b = 0.1
    # y = a*pow(b,x)
    # p3 = plt.loglog(x, y, label="Exponential Decay")

    ##########################################################################################################################

    x = np.linspace(1, 1000, 1000)
    y = np.zeros(1000)
    a = 2
    alpha_1 = 0.9
    alpha_2 = -1
    for i in range(0,1000,50):
        y[i:i+35] = a*pow(x[0:35],-alpha_1)
        y[i+35:i+50] = y[i+34]*pow(x[0:15],-alpha_2)
        a = y[i+49]
    p4 = plt.loglog(x, y, label="Power-Law Decay with Periodicity")

    ##########################################################################################################################
    ax = plt.axes()
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, prop={'size': 15})
    plt.tick_params(labelsize='large', width=3)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax.set_xlim(1.0, 1000.0)
    # ax.set_ylim(0.1, 3)
    ax.set_xlabel('Distance between symbol, d', fontsize=20)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=20)
    plt.savefig('standard_pl_periodic', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()