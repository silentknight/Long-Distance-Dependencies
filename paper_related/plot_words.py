#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["penn_tree","text8","text8_wor","text8_subset","text8_subset_wor","wiki2","wiki2_raw","wiki2_cleaned", \
            "wiki19","wiki19_Text8","wiki103","wiki103_raw","wiki103_cleaned","wiki_sample_1","wiki_sample_2", \
            "wiki_PTB_size_1","wiki_PTB_size_2","wiki_PTB_vocab_1","wiki_PTB_vocab_2","10kGNAD"]

all_mi = []
all_hx = []
all_hy = []
all_hxy = []

for filename in filenames:
    f = open(filename+"_words_10000_grassberger_logx_mi.dat", "r")
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

    plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], color='red', linestyle='solid', label="PTB")

    # plt.loglog(np.arange(1,len(all_mi[1])+1), all_mi[1], color='fuchsia', linestyle='solid', label="Text8")
    # plt.loglog(np.arange(1,len(all_mi[2])+1), all_mi[2], color='indigo', linestyle='solid', label="Text8 (w/ Rare)")
    # plt.loglog(np.arange(1,len(all_mi[3])+1), all_mi[3], color='pink', linestyle='solid', label="Text8 (Subset)")
    # plt.loglog(np.arange(1,len(all_mi[4])+1), all_mi[4], color='purple', linestyle='solid', label="Text8 (w/ Rare Ssubset)")

    plt.loglog(np.arange(1,len(all_mi[5])+1), all_mi[5], color='blue', linestyle='solid', label="Wiki2")
    # plt.loglog(np.arange(1,len(all_mi[6])+1), all_mi[6], color='darkblue', linestyle='solid', label="Wiki2 (Raw)")
    # plt.loglog(np.arange(1,len(all_mi[7])+1), all_mi[7], color='cyan', linestyle='solid', label="Wiki2 (Cleaned)")

    # plt.loglog(np.arange(1,len(all_mi[8])+1), all_mi[8], color='brown', linestyle='solid', label="Wiki19")
    # plt.loglog(np.arange(1,len(all_mi[9])+1), all_mi[9], color='khaki', linestyle='solid', label="Wiki19 (Text8)")

    # plt.loglog(np.arange(1,len(all_mi[10])+1), all_mi[10], color='yellowgreen', linestyle='solid', label="Wiki103")
    # plt.loglog(np.arange(1,len(all_mi[11])+1), all_mi[11], color='darkgreen', linestyle='solid', label="Wiki103 (Raw)")
    # plt.loglog(np.arange(1,len(all_mi[12])+1), all_mi[12], color='lightgreen', linestyle='solid', label="Wiki103 (Cleaned)")

    plt.loglog(np.arange(1,len(all_mi[13])+1), all_mi[13], color='aqua', linestyle='solid', label="Wiki Sample 1")
    plt.loglog(np.arange(1,len(all_mi[14])+1), all_mi[14], color='cyan', linestyle='solid', label="Wiki Sample 2")
    plt.loglog(np.arange(1,len(all_mi[15])+1), all_mi[15], color='magenta', linestyle='solid', label="Wiki PTB Size 1")
    plt.loglog(np.arange(1,len(all_mi[16])+1), all_mi[16], color='green', linestyle='solid', label="Wiki PTB Size 2")
    plt.loglog(np.arange(1,len(all_mi[17])+1), all_mi[17], color='black', linestyle='solid', label="Wiki PTB Vocabulary 1")
    plt.loglog(np.arange(1,len(all_mi[18])+1), all_mi[18], color='grey', linestyle='solid', label="Wiki PTB Vocabulary 2")

    # plt.loglog(np.arange(1,len(all_mi[19])+1), all_mi[19], color='yellow', linestyle='solid', label="German Text")

    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    ax.set_xlim(1, len(all_mi[0]))
    ax.set_ylim(0.56, 3.2)
    print(ax.get_xlim())
    print(ax.get_ylim())
    ax.set_xlabel('Distance between words, d', fontsize=15)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=15)
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})
    plt.savefig('lm_words_ptb_type', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
