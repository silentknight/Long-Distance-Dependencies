#!/usr/bin/env python

# System libs
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import argparse
import sys
import os
import re
import ast
import scipy.sparse
import json

parser = argparse.ArgumentParser(description='Pointwise Mutual Information Processing file.')
parser.add_argument('--pmi_path', type=str, default='pmi_data/log_data', help='Path of the pmi folder')
parser.add_argument('--subseq_path', type=str, default='pmi_data/log_data', help='Path of the subsequences')
parser.add_argument('--logscale', type=int, default=1, help='Plot on Log Scale or normal scale. 1: Log Scale; 0: Normal Scale')
parser.add_argument('--normalize', type=str, default='n', help='Normalize values')
args = parser.parse_args()

####################################################################################################
# Open and read subsequences obtained while computing Fano's inequality                            #
####################################################################################################
f = open(args.subseq_path,'r')
data = f.read()
f.close()
subsequences = json.loads(data)

try:
	f = open(args.pmi_path+"/0.symbols.dat", 'r')
	data = f.read()
	symbols = ast.literal_eval(data)
	f.close()
except:
	print(args.pmi_path+" does not exist. Please check the path. Do not add / at the end of the path.")
	sys.exit()

for subsequence in subsequences:
	
	pmi_vector = np.empty((0,1))
	Ni_XY_vector = np.empty((0,1))
	
	for i in range(len(subsequence)):
		for j in range(i+1,len(subsequence)):
			d = abs(i-j)

			char1_ID = int(symbols[str(subsequence[i])])
			char2_ID = int(symbols[str(subsequence[j])])

			if not os.path.exists(os.path.join(args.pmi_path, "pmi", str(d)+".npz")):
				print("File at D=%d is absent. Re-run PMI computations" % d)
				sys.exit()
				
			pmi_data = np.load(os.path.join(args.pmi_path, "np", str(d)+".npz"), mmap_mode='r')
			Xi = pmi_data['arr_0']
			Yi = pmi_data['arr_1']
			# Ni_X = pmi_data['arr_2']
			# Ni_Y = pmi_data['arr_3']

			Ni_XY = scipy.sparse.load_npz(os.path.join(args.pmi_path, "Ni_XY", str(d)+".npz"))
			pmi = scipy.sparse.load_npz(os.path.join(args.pmi_path, "pmi", str(d)+".npz"))

			pmi_vector = np.append(pmi_vector, pmi[np.where(Xi==char1_ID)[0][0],np.where(Yi==char2_ID)[0][0]])
			Ni_XY_vector = np.append(Ni_XY_vector, Ni_XY[np.where(Xi==char1_ID)[0][0],np.where(Yi==char2_ID)[0][0]])

	print(pmi_vector)
	print(Ni_XY_vector)

	if not len(pmi_vector) == 0:
		ax = plt.subplot(211)
		if len(pmi_vector) == 1:
			plt.bar(np.arange(len(pmi_vector)),pmi_vector)
		elif len(pmi_vector) > 1:
			plt.plot(pmi_vector)
		ax.grid(True)

		ax = plt.subplot(212)
		if len(Ni_XY_vector) == 1:
			plt.bar(np.arange(len(Ni_XY_vector)),Ni_XY_vector)
		elif len(Ni_XY_vector) > 1:
			plt.plot(Ni_XY_vector)
		ax.grid(True)

		plt.show()