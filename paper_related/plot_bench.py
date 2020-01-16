#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["mnist_un","mnist","mnist_per_1","mnist_per_2"]
all_mi = []

for filename in filenames:
    f = open(filename+"_grassberger_logx_mi.dat", "r")
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

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):
    plt.loglog(np.arange(len(all_mi[0])), all_mi[0], label='Standard MNIST')
    plt.loglog(np.arange(len(all_mi[1])), all_mi[1], label='Permuted MNIST 1')
    plt.loglog(np.arange(len(all_mi[2])), all_mi[2], label='Permuted MNIST 2')
    plt.loglog(np.arange(len(all_mi[3])), all_mi[3], label='Permuted MNIST 3')
    
    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    ax.set_xlim(1, len(all_mi[0]))
    print(ax.get_xlim())
    print(ax.get_ylim())
    ax.set_xlabel('Distance between pixels, d', fontsize=15)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=15)
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=1, numpoints=1) 
    plt.savefig('mnist', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()