#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["unperm_mnist_char","perm_mnist_char"]
all_mi = []

for filename in filenames:
    f = open("../datapoints/"+filename+".log", "r")
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
    p1, p2 = plt.loglog(np.arange(len(all_mi[0])), all_mi[0], np.arange(len(all_mi[1])), all_mi[1])
    plt.tick_params(labelsize='large', width=3)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    plt.xlim(0, 1000)

    ax = plt.axes()
    ax.set_xlabel('Distance between reshaped pixels, D(X,Y)', fontsize=15)
    ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)
    lgd = ax.legend((p1, p2), ("Unpermuted MNIST data","Permuted MNIST data"), loc='lower left', shadow=True, fancybox=True)

    plt.savefig('mnist', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
