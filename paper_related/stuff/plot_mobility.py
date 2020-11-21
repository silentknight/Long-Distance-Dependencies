#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["taxi_1_1","taxi_2_1","taxi_3_1","user_grids"]
all_mi = []

for filename in filenames:
    f = open(filename+".log", "r")
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
    p1, p2, p3, p4 = plt.loglog(np.arange(len(all_mi[0])), all_mi[0], np.arange(len(all_mi[1])), all_mi[1], np.arange(len(all_mi[2])), all_mi[2], np.arange(len(all_mi[3])), all_mi[3])
    plt.tick_params(labelsize='large', width=3)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')

    ax = plt.axes()
    ax.set_xlabel('Distance between location samples, D(X,Y)', fontsize=15)
    ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)
    lgd = ax.legend((p1, p2, p3, p4), ("Taxi 1","Taxi 2","Taxi 3","User Mobility"), loc='lower left', shadow=True, fancybox=True)

    plt.savefig('mobility', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
