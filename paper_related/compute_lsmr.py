#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats
import argparse

parser = argparse.ArgumentParser(description='PyTorch Transformer Language Model')
parser.add_argument('--fileID', type=int, required=True, help='ID of the filename to analyze')
parser.add_argument('--end_point', type=int, help='End Point calculation')
args = parser.parse_args()

files = np.array([('penn_tree', 622, 4), ('text8', 1208, 4), ('text8_wor', 1150, 4), ('text8_subset', 1470, 4), ('text8_subset_wor', 1070, 4) , ('wiki2', 2203, 4), ('wiki2_raw', 2158, 4), \
		('wiki2_cleaned', 1330, 4), ('wiki19', 2436, 4), ('wiki19_text8', 2170, 4), ('wiki103', 2989, 4), ('wiki103_raw', 3020, 4), ('wiki103_cleaned', 3067, 4), ('wiki_ptb_size_1', 1288, 4), \
		('wiki_ptb_size_2', 1253, 4),('wiki_ptb_vocab_1', 1860, 4), ('wiki_ptb_vocab_2', 1319, 4), ('10kGNAD', 470, 5), ('wiki_sample_1', 1100, 4), ('wiki_sample_2', 1159, 4), \
		('wiki_sample_3', 1142, 4), ('wiki_sample_4', 1314, 4), ('wiki_sample_3_check', 1715, 4), ('wiki_sample_4_check', 0, 4), ('wiki19_text8_wor', 0, 4), ('text8_subset_wor_4', 0, 4)],
		dtype=[('filename', (np.str_, 20)), ('d_doc', np.int32), ('thr', np.int32)])

filename = files[args.fileID]['filename']
filename += '_words_10000_grassberger_logx_mi.dat'

f = open(filename, 'r')
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
if temp[0] == 'data:':
	for line in lines:
		temp = line.strip().split(':')
		if temp[0] == 'd':
			temp1 = temp[2].split(',')
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
	print('Not a valid file')

if args.end_point is not None:
	end_point = args.end_point
else:
	end_point = files[args.fileID]['d_doc']

sdds = 0
ldds = 0
threshold = files[args.fileID]['thr']
sdds = np.sum(mi[0:threshold])
ldds = np.sum(mi[threshold:end_point])

print('Dataset:', filename)
print('Break Point 1:', threshold)
print('Break Point 2:', end_point)
print('SDDs', sdds)
print('LDDs', ldds)
print('SDDs/LDDs:', sdds/ldds)
print('LDDs/SDDs:', ldds/sdds)