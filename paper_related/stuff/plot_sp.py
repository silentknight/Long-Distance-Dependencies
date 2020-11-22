#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["sp2_20_char","sp2_100_char","sp2_200_char","sp2_500_char","sp4_100_char","sp16_100_char","sp2_20_v26_char","sp2_20_char_f_mi","sp2_20_char_size_mi"]

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

    all_mi.append(np.abs(mi).tolist())

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):
    # plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], label="SP2 20")
    plt.loglog(np.arange(1,len(all_mi[1])+1), all_mi[1], label="SP2 100")
    # plt.loglog(np.arange(1,len(all_mi[2])+1), all_mi[2], label="SP2 200")
    # plt.loglog(np.arange(1,len(all_mi[3])+1), all_mi[3], label="SP2 500")
    plt.loglog(np.arange(1,len(all_mi[4])+1), all_mi[4], label="SP4 100")
    plt.loglog(np.arange(1,len(all_mi[5])+1), all_mi[5], label="SP16 100")
    #plt.loglog(np.arange(1,len(all_mi[6])+1), all_mi[6], label="SP2 20 V26")
    #plt.loglog(np.arange(1,len(all_mi[7])+1), all_mi[7], label="SP2 20 FS={ab,bc,cd,dc}")
    #plt.loglog(np.arange(1,len(all_mi[8])+1), all_mi[8], label="SP2 20 Small")

    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    # ax.set_xlim(1, len(all_mi[0]))
    # ax.set_ylim(-0.005, 0.06)
    print(ax.get_xlim())
    print(ax.get_ylim())
    ax.set_xlabel('Distance between symbols, d', fontsize=15)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=15)
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=2, numpoints=1, prop={'size': 12})
    plt.savefig('spk_k', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
