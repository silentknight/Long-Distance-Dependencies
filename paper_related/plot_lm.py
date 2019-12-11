#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from astropy.modeling import models
from scipy import stats

# filenames = ["enwik8_letters_","penn_tree_letters_","text8_letters_","wiki2_letters_","wiki103_letters_"]
# filenames = ["penn_tree_words","text8_words","text8_subset_words","text8_wo_rare_words","text8_wo_rare_subset_words","wiki2_words","wiki2_cleaned_words","wiki103_words","wiki103_cleaned_words"]
# filenames = ["enwik8_letters_15000","penn_tree_letters_15000","wiki2_letters_15000"]
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

######################################################################################################################
break_point = [4,4,5,4]
end_point = [200,200,200,200]
for dataset in range(len(filenames)):

    sdds = 0
    ldds = 0

    for i in range(break_point[dataset]):
        sdds += all_mi[dataset][i]

    for i in range(break_point[dataset],end_point[dataset]):
        ldds += all_mi[dataset][i]

    print("\n")
    print("Dataset", dataset)
    print("SDDs", sdds)
    print("LDDs", ldds)
    print("Proportional", sdds/ldds, ldds/sdds)

########################################################################################################################
# with plt.style.context(('seaborn')):

    ####################################################################################################################
    # break_point = 4
    # dataset = 0
    # alpha_1 = 0.4785
    # alpha_2 = 0.00801
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.3
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="Penn TreeBanks")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Penn TreeBank")

    # break_point = 4
    # dataset = 1
    # alpha_1 = 0.4811
    # alpha_2 = 0.016
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.228
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="Text8")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8")

    # break_point = 4
    # dataset = 2
    # alpha_1 = 0.421
    # alpha_2 = 0.0028
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.346
    # fit_sample = f(x)
    # p3 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="WikiText2")
    # p4 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2")

    # break_point = 5
    # dataset = 3
    # alpha_1 = 0.6931
    # alpha_2 = 0.019
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.35
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="WikiText103")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText103")

#     #######################################################################################################################
#     break_point = 30
#     dataset = 2
#     alpha_1 = 2.1
#     alpha_2 = 0.29
#     amplitude = all_mi[dataset][break_point-1]
#     x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
#     f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
#     f.delta = 0.1
#     fit_sample = f(x)

#     # plt.subplot(221)
#     p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="LDD Curve")
#     p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law")
#     # plt.grid(True)

#     # plt.subplot(222)
#     # p3 = plt.loglog(np.arange(1,len(all_Hxy[dataset])+1), all_Hxy[dataset])
#     # plt.grid(True)

#     # plt.subplot(223)
#     # p4 = plt.loglog(np.arange(1,len(all_Hx[dataset])+1), all_Hx[dataset])
#     # plt.grid(True)

#     # plt.subplot(224)
#     # p5 = plt.loglog(np.arange(1,len(all_Hy[dataset])+1), all_Hy[dataset])
#     # plt.grid(True)

#     #########################################################################################################################
#     ax = plt.axes()
#     lgd = ax.legend(loc='upper right', shadow=True, fancybox=True) 
#     plt.tick_params(labelsize='large', width=3)
#     plt.grid(True)
#     plt.grid(which='major', linestyle='-', linewidth='0.1', color='grey')
#     plt.grid(which='minor', linestyle='-', linewidth='0.1', color='grey')
#     # ax.set_xlim(1, len(all_mi[0]))
#     ax.set_xlabel('Distance between words, D(X,Y)', fontsize=15)
#     ax.set_ylabel('Mutual Information, I(X,Y)', fontsize=15)
#     # plt.savefig('fit', bbox_extra_artists=(lgd,), bbox_inches='tight')
#     plt.show()

# #########################################################################################################################
# [D, p_value] = stats.ks_2samp(all_mi[dataset], fit_sample)

# print("")
# print("Dataset", dataset)
# print("D_inf", break_point)
# print("c1",all_mi[dataset][0])
# print("alpha 1", alpha_1)
# print("amplitude", all_mi[dataset][break_point-1])
# print("alpha 2", alpha_2)
# print("delta", f.delta)
# print("D", D)
# print("p-value", p_value)