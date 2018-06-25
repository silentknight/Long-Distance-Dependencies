#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# filenames = ["enwik8_char","ptb_char","text8_char","wiki2_char","wiki103_char"]
filenames = ["ptb_words","wiki2_words"]
all_mi = []

for filename in filenames:
    f = open("datapoints/"+filename+".log", "r")
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

    all_mi.append(mi[0:1000].tolist())

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):
    # p1, p2, p3, p4, p5 = plt.loglog(np.arange(len(all_mi[0])), all_mi[0], np.arange(len(all_mi[1])), all_mi[1], np.arange(len(all_mi[2])), all_mi[2], np.arange(len(all_mi[3])), all_mi[3], np.arange(len(all_mi[4])), all_mi[4])
    p1, p2 = plt.loglog(np.arange(len(all_mi[0])), all_mi[0], np.arange(len(all_mi[1])), all_mi[1])
    plt.tick_params(labelsize='large', width=3)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')

    ax = plt.axes()
    ax.set_xlabel('Distance between words, D(X,Y)', fontsize=15)
    ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)
    # lgd = ax.legend((p1, p2, p3, p4, p5), ("enwik8 characters","PennTree Banks characters","text8 characters","WikiText 2 characters","WikiText 103 characters"), loc='lower left', shadow=True, fancybox=True)
    lgd = ax.legend((p1, p2), ("PennTree Banks Words","WikiText 2 Words"), loc='upper right', shadow=True, fancybox=True)

    plt.savefig('lm_words', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
