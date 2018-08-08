#!/usr/bin/env python

# System libs
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import os
import re

parser = argparse.ArgumentParser(description='Long Distance Dependency measurements plot')
parser.add_argument('--path', type=str, default='pmi_data/log_data', help='Path of the data file')
parser.add_argument('--start', type=int, default=1, help='Value of D (Dependency distance) from start for plotting. Default is 1')
parser.add_argument('--end', type=str, default='end', help='Value of D (Dependency distance) till end for plotting. Default is \'end\' (all the way will the end).')
parser.add_argument('--logscale', type=int, default=1, help='Plot on Log Scale or normal scale. 1: Log Scale; 0: Normal Scale')
parser.add_argument('--normalize', type=str, default='n', help='Normalize values')
parser.add_argument('--char1', type=str, help='Character you want to find the distribution', required=True)
parser.add_argument('--char2', type=str, help='Character against which you want to find the distribution', required=True)
args = parser.parse_args()

####################################################################################################
# Open the symbols file and check if the characters are present which are supplied in command line #
####################################################################################################
try:
	good1 = False
	good2 = False
	charID_1 = -1
	charID_2 = -1

	f = open(args.path+"/0.symbols.dat", 'r')
	data = f.read()
	data = data[1:len(data)-2]
	symbols = re.split(", ", data)
	for temp in symbols:
		fields = re.split("': ", temp)
		if args.char1 == fields[0][1]:
			good1 = True
			charID_1 = int(fields[1])
		if args.char2 == fields[0][1]:
			good2 = True
			charID_2 = int(fields[1])
	f.close()

	if good1 and good2:
		print("Characters you supplied found, "+args.char1+": "+str(charID_1)+" and "+args.char1+": "+str(charID_2)+".")
	else:
		print("Characters you supplied are not present in the dataset.")
		sys.exit()

except Exception as e:
	print(e)
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
try:
	d_num = []
	ext = ""
	files = sorted(os.listdir(args.path))
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

except Exception as e:
	print(e)
	print(args.path+" does not exist")

d = start
pmi_single = np.empty((0,1))

for file in files:
	npzfile = np.load(args.path+"/"+file)
	Xi = npzfile['arr_0']
	Yi = npzfile['arr_1']
	Ni_X = npzfile['arr_2']
	Ni_Y = npzfile['arr_3']
	Ni_XY = npzfile['arr_4']
	pmi = npzfile['arr_5']

	pmi_single = np.append(pmi_single, pmi[np.where(Xi==charID_1)[0][0]][np.where(Yi==charID_2)[0][0]])

if args.logscale == 1:
	plt.loglog(np.arange(len(pmi_single)),pmi_single,basex=10)
elif args.logscale == 0:
	plt.plot(pmi_single)
plt.show()