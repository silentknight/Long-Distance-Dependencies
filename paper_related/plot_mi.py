#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats
import sys

filenames = ["penn_tree_words_full_grassberger_logx_mi.dat","wiki2_words_full_grassberger_logx_mi.dat"]
# filenames = ["penn_tree_words_10000_grassberger_logx_mi.dat","penn_tree_words_10000_standard_logx_mi.dat"]
# filenames = ["wiki2_words_10000_grassberger_logx_mi.dat","wiki2_words_10000_standard_logx_mi.dat"]

all_mi = []
all_hx = []
all_hy = []
all_hxy = []



for filename in filenames:
    print("\nProcessing: ", filename)

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    start = 0
    end = 0
    index = 0

    mi = np.zeros([len(lines)-1])
    Hx = np.zeros([len(lines)-1])
    Hy = np.zeros([len(lines)-1])
    Hxy = np.zeros([len(lines)-1])

    temp = lines[0].split()
    if temp[0] == "data:":
        for line in lines:
            temp = line.strip().split(":")
            if temp[0] == "d":
                temp1 = temp[2].split(",")
                mi[int(temp[1])-1] = float(temp1[0])
                Hx[int(temp[1])-1] = float(temp1[1])
                Hy[int(temp[1])-1] = float(temp1[2])
                Hxy[int(temp[1])-1] = float(temp1[3])
                d = int(temp[1])+1

                sys.stdout.write("\rProcessed -> d: %d" % (d))
                sys.stdout.flush()
            index+=1
    else:
        print("Not a valid file")

    all_mi.append(mi.tolist())
    all_hx.append(Hx.tolist())
    all_hy.append(Hy.tolist())
    all_hxy.append(Hxy.tolist())

with plt.style.context(('seaborn')):
    ax = plt.axes()

    plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], label="PTB Full Length")
    plt.loglog(np.arange(1,len(all_mi[1])+1), all_mi[1], label="Wiki2 Full Length")

    # break_point = 4
    # data = all_mi[0]
    # alpha_1 = 0.4786
    # alpha_2 = 0.01
    # end_point = 622

    # p1 = plt.plot(np.arange(1,len(data)+1), data, "r-", label="PTB")
    # x = np.linspace(0, len(data), len(data))
    
    # amplitude = mi[break_point-1]
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.275
    # fit_sample = f(x)
    # p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law fit for PTB")

    # break_point = 622
    # data = all_mi[0]
    # alpha_1 = 0.01
    # alpha_2 = -0.0008
    # end_point = 100000

    # amplitude = mi[break_point+1]
    # f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # fit_sample = f(x)
    # p2 = plt.plot(x, fit_sample, label="Broken Power-Law fit for PTB")


    # data = all_mi[0][622:]

    # num_values = 10
    # interval = len(data) // (num_values - 1)
    # for i in range(0,len(data),interval):
    #     print(i, np.average(data[i:i+100]))

    # x = np.arange(1, len(data)+1)

    # plt.plot(x,data)

    # # y = 1.0188068606979217 - (-2.927925e-7/-0.000001556964)*(1 - np.exp(+0.00000166*x))
    # y = 1.020439 - (-3.016335e-7/-0.000001490813)*(1 - np.exp(+0.000001490813*x))
    # plt.plot(x,y)

    # [D, p_value] = stats.ks_2samp(data,y)
    # print("D :", D)
    # print("p-value :", p_value)    

    plt.tick_params(labelsize='large', width=10)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    # ax.set_xlim(1, len(all_mi[0]))
    # ax.set_ylim(0.9, 2.7)
    print(ax.get_xlim())
    print(ax.get_ylim())
    ax.set_xlabel('Distance between words (lag), d', fontsize=20)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=20)
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, numpoints=1, prop={'size': 18})
    # plt.savefig('mi_intro_ptb', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
