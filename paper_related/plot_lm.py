#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from astropy.modeling import models
from scipy import stats

# filenames = ["enwik8_letters_","penn_tree_letters_","text8_letters_","wiki2_letters_","wiki103_letters_"]
# filenames = ["penn_tree_words","text8_words","text8_subset_words","text8_wo_rare_words","text8_wo_rare_subset_words","wiki2_words","wiki2_cleaned_words","wiki103_words","wiki103_cleaned_words"]
filenames = ["penn_tree_words_10000","text8_words_10000","wiki2_words_10000","wiki103_words_10000"]

all_mi = []
all_Hx = []
all_Hy = []
all_Hxy = []

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
    all_Hx.append(Hx.tolist())
    all_Hy.append(Hy.tolist())
    all_Hxy.append(Hxy.tolist())

# break_point = [4,4,4,4,4,4,4,5,4]
# for dataset in range(len(filenames)):

#     sdds = 0
#     ldds = 0

#     for i in range(break_point[dataset]):
#         sdds += all_mi[dataset][i]

#     for i in range(break_point[dataset],len(all_mi[dataset])):
#         ldds += all_mi[dataset][i]

#     print("\n")
#     print("Dataset", dataset)
#     print("SDDs", sdds)
#     print("LDDs", ldds)
#     print("Proportional", sdds/ldds, ldds/sdds)

break_point = 4

dataset = 0
alpha_1 = 0.4785
alpha_2 = 0.00801

# dataset = 1
# alpha_1 = 0.4811
# alpha_2 = 0.016

# dataset = 2
# alpha_1 = 0.421
# alpha_2 = 0.0028

# dataset = 3
# alpha_1 = 0.6931
# alpha_2 = 0.019

amplitude = all_mi[dataset][break_point-1]

x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
f.delta = 0.3
# f.delta = 0.228
# f.delta = 0.346
# f.delta = 0.35
fit_sample = f(x)

with plt.style.context(('seaborn')):
    # p1, p2, p3, p4, p5 = plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], np.arange(1,len(all_mi[1])+1), all_mi[1], np.arange(1,len(all_mi[2])+1), all_mi[2], np.arange(1,len(all_mi[3])+1), all_mi[3], np.arange(1,len(all_mi[4])+1), all_mi[4])
    # p1, p2, p3, p4, p5, p6, p7, p8, p9 = plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], np.arange(1,len(all_mi[1])+1), all_mi[1], np.arange(1,len(all_mi[2])+1), all_mi[2], np.arange(1,len(all_mi[3])+1), all_mi[3],np.arange(1,len(all_mi[4])+1), all_mi[4], np.arange(1,len(all_mi[5])+1), all_mi[5], np.arange(1,len(all_mi[6])+1), all_mi[6], np.arange(1,len(all_mi[7])+1), all_mi[7], np.arange(1,len(all_mi[8])+1), all_mi[8])

    # plt.subplot(221)
    p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset])
    p2 = plt.loglog(x, fit_sample)
    # plt.grid(True)

    # plt.subplot(222)
    # p3 = plt.loglog(np.arange(1,len(all_Hxy[dataset])+1), all_Hxy[dataset])
    # plt.grid(True)

    # plt.subplot(223)
    # p4 = plt.loglog(np.arange(1,len(all_Hx[dataset])+1), all_Hx[dataset])
    # plt.grid(True)

    # plt.subplot(224)
    # p5 = plt.loglog(np.arange(1,len(all_Hy[dataset])+1), all_Hy[dataset])
    # plt.grid(True)

    ax = plt.axes()
    ax.set_xlabel('Distance', fontsize=15)
    ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)

    [D, p_value] = stats.ks_2samp(all_mi[dataset], fit_sample)

    print("")
    print("Dataset", dataset)
    print("D_inf", break_point)
    print("c1",all_mi[dataset][0])
    print("alpha 1", alpha_1)
    print("amplitude", all_mi[dataset][break_point-1])
    print("alpha 2", alpha_2)
    print("delta", f.delta)
    print("D", D)
    print("p-value", p_value)

    # lgd = ax.legend((p1, p2, p3, p4, p5), ("enwik8 characters","PennTree Banks characters","text8 characters","WikiText 2 characters","WikiText 103 characters"), loc='lower left', shadow=True, fancybox=True)
    # lgd = ax.legend((p1, p2, p3, p4, p5, p6, p7, p8, p9), ("PennTree Banks words","text8 words","text8 small words","text8 w/o rare words","text8 w/o rare small words","WikiText 2 words","WikiText2 cleaned words","WikiText103 words","WikiText103 cleaned words"), loc='lower left', shadow=True, fancybox=True)
    lgd = ax.legend((p1, p2), ("LDD Curve","Smoothly Broken Power-Law"), loc='lower left', shadow=True, fancybox=True)

    plt.show()
