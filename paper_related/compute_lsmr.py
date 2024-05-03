#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats
import argparse

parser = argparse.ArgumentParser(description='PyTorch Transformer Language Model')
parser.add_argument('--end_point', type=int, help='End Point calculation')
args = parser.parse_args()

files = np.array([(0, 'penn_tree', 622, 4, 2.122), (1, 'text8', 1208, 4, 2.353), (2, 'text8_wor', 1150, 4, 2.188), (3, 'text8_subset', 1470, 4, 2.730), (4, 'text8_subset_wor', 1070, 4, 2.380), \
		(5, 'wiki2', 2203, 4, 2.399), (6, 'wiki2_raw', 2158, 4, 2.736), (7, 'wiki2_cleaned', 1330, 4, 2.435), (8, 'wiki103', 2989, 4, 2.186), (9, 'wiki103_raw', 3020, 4, 2.237), (10, 'wiki103_cleaned', 3067, 4, 2.157), \
		(11, 'wiki_sample_1', 1100, 4, 2.456), (12, 'wiki_sample_2', 1159, 4, 2.461), (13, 'wiki_sample_3', 1032, 4, 2.621), (14, 'wiki_sample_4', 1314, 4, 2.398), (15, '10kGNAD', 470, 5, 3.067), \
		(16, 'wiki19', 2436, 4, 2.357), (17, 'wiki19_text8', 2170, 4, 2.217), (18, 'wiki19_text8_wor', 1715, 4, 2.125), (19, 'text8_subset_new', 1470, 4, 2.730), (20, 'text8_subset_wor_2_new', 1070, 4, 2.380)],
		dtype=[('id', np.int32), ('filename', (np.str_, 30)), ('d_doc', np.int32), ('thr', np.int32), ('c1', np.float32)])

for file in files:
	filename = file['filename']
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
		end_point = file['d_doc']

	sdds = 0
	ldds = 0
	threshold = file['thr']
	c1 = file['c1']
	sdds = np.sum(mi[0:threshold])
	ldds = np.sum(mi[threshold:end_point])

	print('-----------------------------------------------------------')
	print('Dataset:', filename)
	print('Break Point 1:', threshold)
	print('Break Point 2:', end_point)
	print('SDDs', sdds)
	print('LDDs', ldds)
	print('SDDs/LDDs:', sdds/ldds)
	print('LDDs/SDDs:', ldds/sdds)
	print('LDDs/SDDs*c1:', ldds/sdds*c1)
	print('-----------------------------------------------------------\n')
