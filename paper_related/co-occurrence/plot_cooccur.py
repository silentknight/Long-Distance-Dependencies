#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["6","8"]

all_hn = []
all_ln = []
all_ind = []
all_lp = []
all_mp = []
all_hp = []

for filename in filenames:
    f = open("cooccur_dataset_"+filename, "r")
    lines = f.readlines()
    f.close()

    start = 0
    end = 0
    index = 0

    hn = np.zeros([0,1])
    ln = np.zeros([0,1])
    ind = np.zeros([0,1])
    lp = np.zeros([0,1])
    mp = np.zeros([0,1])
    hp = np.zeros([0,1])
    temp = lines[0].split()

    for line in lines:
        temp = line.strip().split(",")
        hn = np.append(hn,np.zeros(1))
        hn[index] = int(temp[0])
        ln = np.append(ln,np.zeros(1))
        ln[index] = int(temp[1])
        ind = np.append(ind,np.zeros(1))
        ind[index] = int(temp[2])
        lp = np.append(lp,np.zeros(1))
        lp[index] = int(temp[3])
        mp = np.append(mp,np.zeros(1))
        mp[index] = int(temp[4])
        hp = np.append(hp,np.zeros(1))
        hp[index] = int(temp[5])
        index+=1

    all_hn.append(hn.tolist()[0:3000])
    all_ln.append(ln.tolist()[0:3000])
    all_ind.append(ind.tolist()[0:3000])
    all_lp.append(lp.tolist()[0:3000])
    all_mp.append(mp.tolist()[0:3000])
    all_hp.append(hp.tolist()[0:3000])

with plt.style.context(('seaborn')):

    plt.loglog(np.arange(1,len(all_hn[0])+1), all_hn[0], "r-", label="Wiki2 High Neg")
    plt.loglog(np.arange(1,len(all_ln[0])+1), all_ln[0], 'm-', label="Wiki2 Low Neg")
    plt.loglog(np.arange(1,len(all_ind[0])+1), all_ind[0], 'c-', label="Wiki2 Ind")
    plt.loglog(np.arange(1,len(all_lp[0])+1), all_lp[0], 'b-', label="Wiki2 Low Pos")
    plt.loglog(np.arange(1,len(all_mp[0])+1), all_mp[0], 'g-', label="Wiki2 Mid Pos")
    plt.loglog(np.arange(1,len(all_hp[0])+1), all_hp[0], "k-", label="Wiki2 High Pos")

    plt.loglog(np.arange(1,len(all_hn[1])+1), all_hn[1], "r--", label="Wiki103 High Neg")
    plt.loglog(np.arange(1,len(all_ln[1])+1), all_ln[1], 'm--', label="Wiki103 Low Neg")
    plt.loglog(np.arange(1,len(all_ind[1])+1), all_ind[1], 'c--', label="Wiki103 Ind")
    plt.loglog(np.arange(1,len(all_lp[1])+1), all_lp[1], 'b--', label="Wiki103 Low Pos")
    plt.loglog(np.arange(1,len(all_mp[1])+1), all_mp[1], 'g--', label="Wiki103 Mid Pos")
    plt.loglog(np.arange(1,len(all_hp[1])+1), all_hp[1], "k--", label="Wiki103 High Pos")

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
