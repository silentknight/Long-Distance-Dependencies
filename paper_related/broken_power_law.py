#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats

filenames = ["penn_tree_words_10000","text8_words_10000","text8_subset_words_10000","text8_wor_words_10000","text8_subset_wor_words_10000","wiki2_words_10000","wiki2_cleaned_words_10000","wiki103_words_10000","wiki103_cleaned_words_10000"]
# filenames = ["enwik8_letters_15000","penn_tree_letters_15000","wiki2_letters_15000"]

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

#######################################################################################################################
with plt.style.context(('seaborn')):

    ###################################################################################################################
    break_point = 4
    dataset = 0
    alpha_1 = 0.4786
    alpha_2 = 0.01
    amplitude = all_mi[dataset][break_point-1]
    x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    f.delta = 0.275
    fit_sample = f(x)
    p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], "r-", label="PTB")
    p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law fit for PTB")

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
    # alpha_1 = 0.305
    # alpha_2 = 0.01
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.19
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="Text8 (S)")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8 (S)")

    # break_point = 4
    # dataset = 3
    # alpha_1 = 0.55
    # alpha_2 = 0.02
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.235
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="Text8 (wR)")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8 (wR)")

    # break_point = 4
    # dataset = 4
    # alpha_1 = 0.42
    # alpha_2 = 0.013
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.19
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="Text8 (wR/S)")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8 (wR/S)")

    # break_point = 4
    # dataset = 5
    # alpha_1 = 0.421
    # alpha_2 = 0.00281
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.346
    # fit_sample = f(x)
    # p3 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="WikiText2")
    # p4 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2")

    # break_point = 4
    # dataset = 6
    # alpha_1 = 0.38215
    # alpha_2 = 0.003
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.25
    # fit_sample = f(x)
    # p3 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="WikiText2 (C)")
    # p4 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 (C)")

    # break_point = 5
    # dataset = 7
    # alpha_1 = 0.694
    # alpha_2 = 0.020
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.345
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="WikiText103")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText103")

    # break_point = 4
    # dataset = 8
    # alpha_1 = 0.77
    # alpha_2 = 0.021
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.35
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="WikiText103 (C)")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText103 (C)")

    #######################################################################################################################
    # break_point = 690
    # dataset = 0
    # alpha_1 = 0.00801
    # alpha_2 = -0.001
    # # amplitude = 0.0004814
    # amplitude = all_mi[dataset][break_point-1]
    # x = np.linspace(1, len(all_mi[dataset]), len(all_mi[dataset]))
    # f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
    # f.delta = 0.1
    # fit_sample = f(x)
    # p1 = plt.loglog(np.arange(1,len(all_mi[dataset])+1), all_mi[dataset], label="LDD Curve")
    # p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law")

    #########################################################################################################################
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
    print("length", len(all_mi[dataset]))
    
    #########################################################################################################################
    ax = plt.axes()
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True) 
    plt.tick_params(labelsize='large', width=3)
    plt.grid(True)
    plt.grid(which='major', linestyle='-', linewidth='0.1', color='grey')
    plt.grid(which='minor', linestyle='-', linewidth='0.1', color='grey')
    ax.set_xlim(1.0, 10000.0)
    ax.set_ylim(0.5665692652625367, 2.840370753962389)
    ax.set_xlabel('Distance between words, d', fontsize=15)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=15)
    plt.savefig('fit', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()

######################################################################################################################
# break_point = [30,30,30,30,30]
# end_point = [1000,1000,1000,1000,1000]
# for dataset in range(len(filenames)):

#     sdds = 0
#     ldds = 0

#     for i in range(break_point[dataset]):
#         sdds += all_mi[dataset][i]

#     for i in range(break_point[dataset],end_point[dataset]):
#         ldds += all_mi[dataset][i]

#     print("\n")
#     print("Dataset", dataset)
#     print("SDDs", sdds)
#     print("LDDs", ldds)
#     print("Proportional", sdds/ldds, ldds/sdds)