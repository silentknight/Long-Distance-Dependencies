#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats
import sys

filename = "penn_tree_words_full_grassberger_logx_mi.dat"

f = open(filename+"", "r")
lines = f.readlines()
f.close()

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

            sys.stdout.write("\rProcessed -> d: %d" % (d))
            sys.stdout.flush()
        index+=1
else:
    print("Not a valid file")


data = mi[622:]
x = np.arange(1, len(data)+1)

Y0 = 1.01809

V0_min = 0.0000003015
V0_max = 0.0000003017
V0_inter = 10000

K_min = 0.0000014
K_max = 0.0000016
K_inter = 10000


for V0 in np.linspace(V0_min,V0_max,V0_inter):
    for K in np.linspace(K_min,K_max,K_inter):

        y = Y0-(-V0/-K)*(1 - np.exp(+K*x))
        [D, p_value] = stats.ks_2samp(data, y)

        # if p_value > 1e-5:
        print("\rY0: %f, V0: %f, K: %f, P Value: %f" % (Y0,V0,K,p_value))