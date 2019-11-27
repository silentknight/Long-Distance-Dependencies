#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

# filenames = ["enwik8_letters_","penn_tree_letters_","text8_letters_","wiki2_letters_","wiki103_letters_"]
filenames = ["penn_tree_words_","text8_words_","text8_subset_words_","text8_wo_rare_words_","text8_wo_rare_subset_words_","wiki2_words_","wiki2_cleaned_words_","wiki103_words_","wiki103_cleaned_words_"]

all_mi = []
for filename in filenames:
    f = open(filename+"grassberger_logx_mi.dat", "r")
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

index = 0
vals = all_mi[index]
plt.loglog(np.arange(1,len(vals)+1), vals)

end1 = 4
vals = all_mi[index][0:end1]
plt.loglog(np.arange(1,len(vals)+1), vals[0]*np.power(np.linspace(1,len(vals)+1,len(vals)),-0.46))

start2 = 8
vals = all_mi[index][start2:]
plt.loglog(np.arange(1,len(vals)+1), vals[0]*np.power(np.linspace(1,len(vals)+1,len(vals)),-0.008))

plt.tick_params(labelsize='large', width=3)
plt.grid(True)

# p1, p2, p3, p4, p5 = plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], np.arange(1,len(all_mi[1])+1), all_mi[1], np.arange(1,len(all_mi[2])+1), all_mi[2], np.arange(1,len(all_mi[3])+1), all_mi[3], np.arange(1,len(all_mi[4])+1), all_mi[4])
#p1, p2, p3, p4, p5, p6, p7, p8, p9 = plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], np.arange(1,len(all_mi[1])+1), all_mi[1], np.arange(1,len(all_mi[2])+1), all_mi[2], np.arange(1,len(all_mi[3])+1), all_mi[3],np.arange(1,len(all_mi[4])+1), all_mi[4], np.arange(1,len(all_mi[5])+1), all_mi[5], np.arange(1,len(all_mi[6])+1), all_mi[6], np.arange(1,len(all_mi[7])+1), all_mi[7], np.arange(1,len(all_mi[8])+1), all_mi[8])

ax = plt.axes()
ax.set_xlabel('Distance', fontsize=15)
ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)

# lgd = ax.legend((p1, p2, p3, p4, p5), ("enwik8 characters","PennTree Banks characters","text8 characters","WikiText 2 characters","WikiText 103 characters"), loc='lower left', shadow=True, fancybox=True)
# lgd = ax.legend((p1, p2, p3, p4, p5, p6, p7, p8, p9), ("PennTree Banks words","text8 words","text8 small words","text8 w/o rare words","text8 w/o rare small words","WikiText 2 words","WikiText2 cleaned words","WikiText103 words","WikiText103 cleaned words"), loc='lower left', shadow=True, fancybox=True)

plt.show()
