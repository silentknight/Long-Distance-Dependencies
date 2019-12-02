#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# filenames = ["wiki103_words_grassberger_logx_mi.dat","wiki2_words_grassberger_logx_mi.dat","penn_tree_words_grassberger_logx_mi.dat","enwik8_words_grassberger_logx_mi.dat","text8_words_grassberger_logx_mi.dat"]
filenames = ["wiki103_words_standard_logx_mi.dat","wiki2_words_100000_standard_logx_mi.dat","penn_tree_words_standard_logx_mi.dat","enwik8_words_standard_logx_mi.dat","text8_words_standard_logx_mi.dat"]
# filenames = ["wiki103_words_standard_log2_mi.dat","wiki2_words_standard_log2_mi.dat","penn_tree_words_standard_log2_mi.dat","enwik8_words_standard_log2_mi.dat","text8_words_standard_log2_mi.dat"]

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

# xnew = np.linspace(1,len(all_mi[0])-1,len(all_mi[0])*2)
# y_smooth = spline(np.arange(len(all_mi[0])),all_mi[0],xnew)    
# p1, p2 = plt.loglog(xnew, y_smooth, np.arange(len(all_mi[1])), all_mi[1])

with plt.style.context(('seaborn')):
    p1, p2, p3, p4, p5 = plt.loglog(np.arange(len(all_mi[0])), all_mi[0], np.arange(len(all_mi[1])), all_mi[1], np.arange(len(all_mi[2])), all_mi[2], np.arange(len(all_mi[3])), all_mi[3], np.arange(len(all_mi[4])), all_mi[4])
    plt.tick_params(labelsize='large', width=3)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    ax.set_xlim(1, len(all_mi[4]))
    ax.set_xlabel('Distance between words, D(X,Y)', fontsize=15)
    ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)
    lgd = ax.legend((p1, p2, p3, p4, p5), ("WikiText 103 words","WikiText 2 words","PennTree Banks words","Enwik8 words","Text8 words"), loc='lower left', shadow=True, fancybox=True) 
    plt.savefig('lm_words', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()

# with plt.style.context(('seaborn')):

#     ax = plt.subplot(2, 1, 1)
#     plt.loglog(np.arange(len(all_mi[4])), all_mi[4], label="Text8 words")
#     plt.loglog(np.arange(len(all_mi[3])), all_mi[3], label="Enwik8 words")
#     plt.loglog(np.arange(len(all_mi[1])), all_mi[1], label="WikiText 2 words")
#     plt.loglog(np.arange(len(all_mi[0])), all_mi[0], label="WikiText 103 words")
#     plt.loglog(np.arange(len(all_mi[2])), all_mi[2], label="PennTree Banks words")
#     # ax = plt.axes()
#     lgd = ax.legend(loc='lower left', shadow=True, fancybox=True) 
#     plt.tick_params(labelsize='large', width=3)
#     plt.grid(True)
#     plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
#     plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
#     ax.set_xlim(1, len(all_mi[4]))
#     # ax.set_xlabel('Distance between words, D(X,Y)', fontsize=15)
#     ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)

#     ax = plt.subplot(2, 1, 2)
#     plt.loglog(np.arange(len(all_hxy[4])), all_hxy[4], label="Text8 words")
#     plt.loglog(np.arange(len(all_hxy[3])), all_hxy[3], label="Enwik8 words")
#     plt.loglog(np.arange(len(all_hxy[1])), all_hxy[1], label="WikiText 2 words")
#     plt.loglog(np.arange(len(all_hxy[0])), all_hxy[0], label="WikiText 103 words")
#     plt.loglog(np.arange(len(all_hxy[2])), all_hxy[2], label="PennTree Banks words")
#     # ax = plt.axes()
#     lgd = ax.legend(loc='lower left', shadow=True, fancybox=True)
#     plt.tick_params(labelsize='large', width=3)
#     plt.grid(True)
#     plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
#     plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
#     ax.set_xlim(1, len(all_hxy[4]))
#     ax.set_xlabel('Distance between words, D(X,Y)', fontsize=15)
#     ax.set_ylabel('Entropy, H(X,Y)', fontsize=15)

#     plt.savefig('lm_words', bbox_extra_artists=(lgd,), bbox_inches='tight')
#     plt.show()