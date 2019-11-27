#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from astropy.modeling import models
from scipy import stats

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

break_point = 4
dataset = 6

x = np.linspace(1, 1000, 1000)
f = models.SmoothlyBrokenPowerLaw1D(amplitude=all_mi[dataset][break_point-1], x_break=break_point, alpha_1=0.361, alpha_2=0.0035)
f.delta = 0.26
fit_sample = f(x)

# p1, p2, p3, p4, p5 = plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], np.arange(1,len(all_mi[1])+1), all_mi[1], np.arange(1,len(all_mi[2])+1), all_mi[2], np.arange(1,len(all_mi[3])+1), all_mi[3], np.arange(1,len(all_mi[4])+1), all_mi[4])
# p1, p2, p3, p4, p5, p6, p7, p8, p9 = plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], np.arange(1,len(all_mi[1])+1), all_mi[1], np.arange(1,len(all_mi[2])+1), all_mi[2], np.arange(1,len(all_mi[3])+1), all_mi[3],np.arange(1,len(all_mi[4])+1), all_mi[4], np.arange(1,len(all_mi[5])+1), all_mi[5], np.arange(1,len(all_mi[6])+1), all_mi[6], np.arange(1,len(all_mi[7])+1), all_mi[7], np.arange(1,len(all_mi[8])+1), all_mi[8])

p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset])
p2 = plt.loglog(x, fit_sample)

ax = plt.axes()
ax.set_xlabel('Distance', fontsize=15)
ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)

[D, p_value] = stats.ks_2samp(all_mi[dataset], fit_sample)

print("")
print("amplitude", all_mi[dataset][break_point-1])
print("D", D)
print("p-value", p_value)

# lgd = ax.legend((p1, p2, p3, p4, p5), ("enwik8 characters","PennTree Banks characters","text8 characters","WikiText 2 characters","WikiText 103 characters"), loc='lower left', shadow=True, fancybox=True)
# lgd = ax.legend((p1, p2, p3, p4, p5, p6, p7, p8, p9), ("PennTree Banks words","text8 words","text8 small words","text8 w/o rare words","text8 w/o rare small words","WikiText 2 words","WikiText2 cleaned words","WikiText103 words","WikiText103 cleaned words"), loc='lower left', shadow=True, fancybox=True)

plt.show()
