#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["1","6","8"]

all_sn = []
all_wn = []
all_ind = []
all_wp = []
all_mp = []
all_sp = []

for filename in filenames:
    f = open("word_pair_dependence_"+filename, "r")
    lines = f.readlines()
    f.close()

    start = 0
    end = 0
    index = 0

    sn = np.zeros([0,1])
    wn = np.zeros([0,1])
    ind = np.zeros([0,1])
    wp = np.zeros([0,1])
    mp = np.zeros([0,1])
    sp = np.zeros([0,1])
    temp = lines[0].split()

    for line in lines:
        temp = line.strip().split(",")
        sn = np.append(sn,np.zeros(1))
        sn[index] = int(temp[0])
        wn = np.append(wn,np.zeros(1))
        wn[index] = int(temp[1])
        ind = np.append(ind,np.zeros(1))
        ind[index] = int(temp[2])
        wp = np.append(wp,np.zeros(1))
        wp[index] = int(temp[3])
        mp = np.append(mp,np.zeros(1))
        mp[index] = int(temp[4])
        sp = np.append(sp,np.zeros(1))
        sp[index] = int(temp[5])
        index+=1

    all_sn.append(sn.tolist()[0:3000])
    all_wn.append(wn.tolist()[0:3000])
    all_ind.append(ind.tolist()[0:3000])
    all_wp.append(wp.tolist()[0:3000])
    all_mp.append(mp.tolist()[0:3000])
    all_sp.append(sp.tolist()[0:3000])

with plt.style.context(('seaborn')):

    plt.loglog(np.arange(1,len(all_hn[0])+1), all_hn[0], "r-", label="Strong Negative")
    plt.loglog(np.arange(1,len(all_ln[0])+1), all_ln[0], 'm-', label="Weak Negative")
    plt.loglog(np.arange(1,len(all_ind[0])+1), all_ind[0], 'c-', label="Independent")
    plt.loglog(np.arange(1,len(all_lp[0])+1), all_lp[0], 'b-', label="Weak Positive")
    plt.loglog(np.arange(1,len(all_mp[0])+1), all_mp[0], 'g-', label="Moderate Positive")
    plt.loglog(np.arange(1,len(all_hp[0])+1), all_hp[0], "k-", label="Strong Positive")

    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    ax.set_xlim(1, len(all_mi[0]))
    # ax.set_ylim(0.56, 3.2)
    print(ax.get_xlim())
    print(ax.get_ylim())
    ax.set_xlabel('Distance between words, d', fontsize=15)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=15)
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})
    plt.savefig('pmi_plots', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
