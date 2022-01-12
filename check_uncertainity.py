#!/usr/bin/env python

# System libs
import seaborn as sns
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
parser.add_argument('--plot', type=int, default=1, help='Display plot. 1: Display; 0: Hide')
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

	xticks_labels = []
	pmi_vector = np.empty((0,1))
	Ni_XY_vector = np.empty((0,1))

	for i in range(len(subsequence)):
		for j in range(i+1,len(subsequence)):
			d = abs(i-j)
			xticks_labels.append(str(i)+','+str(j))

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

	print('The accumulated value = %f' % np.sum(pmi_vector))
	print('The weighted accumulated value = %f' % (np.sum(pmi_vector)/pmi_vector.size))
	print('The vector is %s' % pmi_vector)
	print('-' * 100)

	with plt.style.context(('seaborn')):
		if args.plot == 1:
			if not len(pmi_vector) == 0:
				ax = plt.subplot(211)
				plt.bar(np.arange(len(pmi_vector)),pmi_vector)
				plt.xticks(np.arange(len(xticks_labels)), xticks_labels)
				plt.tick_params(labelsize='large', width=3)
				plt.grid(True)
				plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
				plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
				ax.set_title("PMI values")
				# ax.set_xlabel('Elements at indexes (i,j)', fontsize=15)
				ax.set_ylabel('PMI in nats', fontsize=15)

				ax = plt.subplot(212)
				plt.bar(np.arange(len(Ni_XY_vector)),Ni_XY_vector)
				plt.xticks(np.arange(len(xticks_labels)), xticks_labels)
				ax.grid(True)
				plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
				plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
				ax.set_title("Ni XY")
				ax.set_xlabel('Elements at indexes (i,j)', fontsize=15)
				ax.set_ylabel('Frequency of occurence', fontsize=15)

				plt.show()
