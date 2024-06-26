#!/usr/bin/env python

import numpy as np
from astropy.modeling import models
from scipy import stats
import sys

filenames = ["penn_tree","text8","text8_wor","text8_subset","text8_subset_wor","wiki2","wiki2_raw","wiki2_cleaned","wiki19","wiki19_text8","wiki103","wiki103_raw","wiki103_cleaned",
             "wiki_sample_1","wiki_sample_2","wiki_ptb_size_1","wiki_ptb_size_2","wiki_ptb_vocab_1","wiki_ptb_vocab_2","10kGNAD","wiki19_cleaned","wiki_sample_3","wiki_sample_4","wiki19_text8_wor"]

filename = filenames[21]
f = open(filename+"_words_10000_grassberger_logx_mi.dat", "r")
lines = f.readlines()
f.close()

start = 0
end = 0
index = 0

mi = np.zeros([len(lines)-1])
Hx = np.zeros([len(lines)-1])
Hy = np.zeros([len(lines)-1])
Hxy = np.zeros([len(lines)-1])

temp = lines[0].split()
if temp[0] == "data:":
    for line in lines:
        temp = line.strip().split(":")
        if temp[0] == "d":
            temp1 = temp[2].split(",")
            mi[int(temp[1])-1] = float(temp1[0])
            Hx[int(temp[1])-1] = float(temp1[1])
            Hy[int(temp[1])-1] = float(temp1[2])
            Hxy[int(temp[1])-1] = float(temp1[3])
            d = int(temp[1])+1
        index+=1
else:
    print("Not a valid file")

print(filename)

alpha_1_min = 0.375
alpha_1_max = 0.375
alpha_1_inter = 1

alpha_2_min = 0.002475
alpha_2_max = 0.002475
alpha_2_inter = 1

delta_min = 0.351
delta_max = 0.351
delta_inter = 1

end_min = 1
end_max = 4000

break_point = 4

for end in range(end_min,end_max):
    print("Computing for data range 0->%d" % end)
    data = mi[0:end]
    x = np.linspace(1, len(data), len(data))
    amplitude = mi[break_point-1]

    for delta in np.linspace(delta_min,delta_max,delta_inter):
        for alpha_1 in np.linspace(alpha_1_min,alpha_1_max,alpha_1_inter):
            for alpha_2 in np.linspace(alpha_2_min,alpha_2_max,alpha_2_inter):
                f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
                f.delta = delta
                fit_sample = f(x)
                [D, p_value] = stats.ks_2samp(data, fit_sample)

                if p_value > 1e-5:
                    print("\rdelta: %f, alpha1: %f, alpha2: %f, P Value: %f" % (delta,alpha_1,alpha_2,p_value))