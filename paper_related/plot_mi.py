#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats
import sys

filenames = ["wiki2_words_full_grassberger_logx_mi.dat"]
# filenames = ["penn_tree_words_full_grassberger_logx_mi.dat"]
# filenames = ["penn_tree_words_10000_grassberger_logx_mi.dat","penn_tree_words_10000_standard_logx_mi.dat"]
# filenames = ["wiki2_words_10000_grassberger_logx_mi.dat","wiki2_words_10000_standard_logx_mi.dat"]

all_mi = []
all_hx = []
all_hy = []
all_hxy = []

for filename in filenames:
    print("Processing: ", filename)

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    if filename=="penn_tree_words_full_grassberger_logx_mi.dat":
        lines = lines[:-(len(lines)-10000)]
        end_point = 622+460
    if filename=="wiki2_words_full_grassberger_logx_mi.dat":
        lines = lines[:-(len(lines)-195500)]
        end_point = 2203+1920

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

        print("")
    else:
        print("Not a valid file")

    with plt.style.context(('seaborn')):
        ax = plt.axes()

        plt.loglog(np.arange(1,len(mi)+1), mi, label=filename)

        # print(end_point,index)
        # data = mi[end_point:]

        # x_inter = []
        # y_inter = []
        # num_values = 500
        # interval = len(data)//(num_values-1)
        # for i in range(0,len(data),interval):
        #     x_inter.append(i+1)
        #     y_inter.append(np.average(data[i:i+10]))
        # print(x_inter)
        # print(y_inter)

        # x = np.arange(0, len(data))

        # plt.plot(x,data)
        # plt.plot(x_inter,y_inter)

        # if filename=="wiki2_words_full_grassberger_logx_mi.dat":
        #     y = 1.299531 - (-1.545001e-7/-0.000001448557)*(1 - np.exp(+0.000001448557*x))

        # if filename=="penn_tree_words_full_grassberger_logx_mi.dat":
        #     # y = 1.018051 - (-2.13736e-7/-0.0001043437)*(1 - np.exp(+0.0001043437*x))
        #     y = 1.018048 - (-1.859269e-7/-0.0001275087)*(1 - np.exp(+0.0001275087*x))

        # plt.plot(x,y)

        # [D, p_value] = stats.ks_2samp(data,y)
        # print("D :", D)
        # print("p-value :", p_value)    

        plt.tick_params(labelsize='large', width=10)
        plt.grid(True)
        plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
        plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
        # ax.set_xlim(1, len(mi))
        # ax.set_ylim(0.9, 2.7)
        print(ax.get_xlim())
        print(ax.get_ylim())
        ax.set_xlabel('Distance between words (lag), d', fontsize=20)
        ax.set_ylabel('Mutual Information, I(d)', fontsize=20)
        lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, numpoints=1, prop={'size': 18})
        # plt.savefig('mi_intro_ptb', bbox_extra_artists=(lgd,), bbox_inches='tight')
        plt.show()
