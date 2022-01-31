#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# filenames = ["penn_tree_words_10000_grassberger_logx_mi.dat","penn_tree_words_10000_standard_logx_mi.dat"]
filenames = ["wiki2_words_10000_grassberger_logx_mi.dat","wiki2_words_10000_standard_logx_mi.dat"]

all_mi = []
all_hx = []
all_hy = []
all_hxy = []

for filename in filenames:
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    start = 0
    end = 0
    index = 0

    mi = np.zeros([0,1])
    Hx = np.zeros([0,1])
    Hy = np.zeros([0,1])
    Hxy = np.zeros([0,1])
    temp = lines[0].split()
    if temp[0] == "data:":
        for line in lines:
            temp = line.strip().split(":")
            if temp[0] == "d":
                temp1 = temp[2].split(",")
                mi = np.append(mi,np.zeros(1))
                mi[int(temp[1])-1] = float(temp1[0])
                Hx = np.append(Hx,np.zeros(1))
                Hx[int(temp[1])-1] = float(temp1[1])
                Hy = np.append(Hy,np.zeros(1))
                Hy[int(temp[1])-1] = float(temp1[2])
                Hxy = np.append(Hxy,np.zeros(1))
                Hxy[int(temp[1])-1] = float(temp1[3])
                d = int(temp[1])+1
            index+=1
    else:
        print("Not a valid file")

    all_mi.append(mi.tolist())
    all_hx.append(Hx.tolist())
    all_hy.append(Hy.tolist())
    all_hxy.append(Hxy.tolist())

with plt.style.context(('seaborn')):

    plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], label="Using Grassbergers Equation")
    plt.loglog(np.arange(1,len(all_mi[1])+1), all_mi[1], label="Using Shannon's Equation")

    plt.tick_params(labelsize='large', width=10)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    ax.set_xlim(1, len(all_mi[0]))
    ax.set_ylim(0.9, 2.7)
    print(ax.get_xlim())
    print(ax.get_ylim())
    ax.set_xlabel('Distance between words (lag), d', fontsize=20)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=20)
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, numpoints=1, prop={'size': 18})
    plt.savefig('mi_intro_wiki2', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
