#!/usr/bin/env python

# System libs
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import os
import re
import ast
import scipy.sparse

parser = argparse.ArgumentParser(description='Long Distance Dependency measurements plot')
parser.add_argument('--path', type=str, default='pmi_data/log_data', help='Path of the data file')
parser.add_argument('--start', type=int, default=1, help='Value of D (Dependency distance) from start for plotting. Default is 1')
parser.add_argument('--end', type=str, default='end', help='Value of D (Dependency distance) till end for plotting. Default is \'end\' (all the way will the end).')
parser.add_argument('--logscale', type=int, default=1, help='Plot on Log Scale or normal scale. 1: Log Scale; 0: Normal Scale')
parser.add_argument('--normalize', type=str, default='n', help='Normalize values')
parser.add_argument('--char1', type=str, help='Character you want to find the distribution', required=True)
parser.add_argument('--char2', type=str, help='Character against which you want to find the distribution')
args = parser.parse_args()

####################################################################################################
# Open the symbols file and check if the characters are present which are supplied in command line #
####################################################################################################
try:
	charID_1 = -1
	charID_2 = -1

	f = open(args.path+"/0.symbols.dat", 'r')
	data = f.read()
	symbols = ast.literal_eval(data)
	if args.char1 in symbols and args.char2 in symbols:
		charID_1 = int(symbols[args.char1])
		charID_2 = int(symbols[args.char2])
		print("Characters you supplied found, "+args.char1+": "+str(charID_1)+" and "+args.char2+": "+str(charID_2)+".")
	elif args.char2 == None:
		charID_1 = int(symbols[args.char1])
		print("Only 1 symbol supplied. Hence computing distribution across all other words.")
	else:
		print("Characters you supplied are not present in the dataset.")
		sys.exit()
	f.close()
except:
	print(args.path+" does not exist. Please check the path. Do not add / at the end of the path.")
	sys.exit()

####################################################################################################
# Get the start and end of "d"                                                                     #
####################################################################################################
start = 1
end = 0

if args.start > 0:
	start = args.start
else:
	print("Start value cannot be less that 1 as Distance cannot be less than 1")
	sys.exit()

try:
	end = int(args.end)
except ValueError:
	if args.end == "end":
		pass
	else:
		print("Not a well formed integer")
		sys.exit()

####################################################################################################
# Get the data from the files                                                                      #
####################################################################################################
print("Pull file list from the folder")
try:
	d_num = []
	ext = ""
	files = sorted(os.listdir(args.path+"/pmi"))
	for file in files:
		d_num.append(int(file.split('.')[0]))
		ext = file.split('.')[1]

	d_num = sorted(d_num)
	files = []
	for file in d_num:
		if args.end == "end":
			if file >= start:
				files.append(str(file)+'.'+ext)
		else:
			if file >= start and file <= end:
				files.append(str(file)+'.'+ext)
except:
	print(args.path+" does not exist")

print("Pull data from numpy file")
d = start
pmi_single = np.empty((0,1))
Ni_XY_single = np.empty((0,1))
pmi_row = []
Ni_XY_row = []

try:
	for file in files:
		pmi_data = np.load(args.path+"/np/"+file, mmap_mode='r')
		Xi = pmi_data['arr_0']
		Yi = pmi_data['arr_1']
		Ni_X = pmi_data['arr_2']
		Ni_Y = pmi_data['arr_3']
		Ni_XY = scipy.sparse.load_npz(args.path+"/Ni_XY/"+file)
		Ni_XY = Ni_XY.todense()
		pmi = scipy.sparse.load_npz(args.path+"/pmi/"+file)
		pmi = pmi.todense()

		if args.char2 == None:
			if pmi_row == []:
				pmi_row = pmi[np.where(Xi==charID_1)[0][0],:]
				Ni_XY_row = Ni_XY[np.where(Xi==charID_1)[0][0],:]
			else:
				pmi_row = np.append(pmi_row, pmi[np.where(Xi==charID_1)[0][0],:], axis=0)
				Ni_XY_row = np.append(Ni_XY_row, Ni_XY[np.where(Xi==charID_1)[0][0],:], axis=0)
		else:
			pmi_single = np.append(pmi_single, pmi[np.where(Xi==charID_1)[0][0],np.where(Yi==charID_2)[0][0]])
			Ni_XY_single = np.append(Ni_XY_single, Ni_XY[np.where(Xi==charID_1)[0][0],np.where(Yi==charID_2)[0][0]])

		print("d:"+str(d)+" -> processed")
		d += 1
except KeyboardInterrupt:
	print("Processing halted. Printing upto d: "+str(d))

if args.char2 == None:
	fig = plt.figure()
	ax = fig.add_subplot(211)
	plt.imshow(pmi_row)
	ax.set_aspect('auto')
	plt.colorbar(orientation='vertical')

	ax = fig.add_subplot(212)
	plt.imshow(Ni_XY_row)
	ax.set_aspect('auto')
	plt.colorbar(orientation='vertical')

	plt.show()
else:
	plt.subplot(211)
	if args.logscale == 1:
		plt.loglog(np.arange(len(pmi_single)),pmi_single,basex=10)
	elif args.logscale == 0:
		plt.plot(pmi_single)
	plt.grid(True)

	plt.subplot(212)
	if args.logscale == 1:
		plt.loglog(np.arange(len(Ni_XY_single)),Ni_XY_single,basex=10)
	elif args.logscale == 0:
		plt.bar(np.arange(len(pmi_single)),Ni_XY_single)
	plt.grid(True)

	plt.show()