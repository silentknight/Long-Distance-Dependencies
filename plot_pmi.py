#!/usr/bin/env python

# System libs
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Long Distance Dependency measurements plot')
parser.add_argument('--path', type=str, default='pmi_data/log_data', help='Path of the data file')
parser.add_argument('--start', type=int, default=1, help='Value of D (Dependency distance) from start for plotting. Default is 1')
parser.add_argument('--end', type=str, default='end', help='Value of D (Dependency distance) till end for plotting. Default is \'end\' (all the way will the end).')
parser.add_argument('--logscale', type=int, default=1, help='Plot on Log Scale or normal scale. 1: Log Scale; 0: Normal Scale')
parser.add_argument('--normalize', type=str, default='n', help='normalize values')
args = parser.parse_args()

start = 0
end = 0

if args.start > 0:
	start = args.start
else:
	print("Start value cannot be less that 1 as Distance cannot be less than 1")
	sys.exit()

if args.end == "end":
	end = len(lines)-1
else:
	try:
		end = int(args.end)
	except ValueError:
		print("Not a well formed integer")
		sys.exit()
	
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
		if file >= start and file <= end:
			files.append(str(file)+'.'+ext)

except  Exception as e:
	print(e)
	print(args.path+" does not exist")

d = start

for file in files:
	npzfile = np.load(file)
	Xi = npzfile['arr_0']
	Yi = npzfile['arr_1']
	Ni_X = npzfile['arr_2']
	Ni_Y = npzfile['arr_3']
	Ni_XY = npzfile['arr_4']
	pmi = npzfile['arr_5']

	
# if args.normalize == "y" or args.normalize == "Y":
# 	x = mi/np.amax(mi)
# else:
# 	x = mi

# plt.subplot(221)
# if args.logscale == 1:
# 	plt.loglog(np.arange(len(x)),x,basex=10)
# elif args.logscale == 0:
# 	plt.plot(x)
# plt.grid(True)

# plt.subplot(222)
# if args.logscale == 1:
# 	plt.semilogx(np.arange(len(Hxy)),Hxy)
# elif args.logscale == 0:
# 	plt.plot(Hxy)
# plt.grid(True)

# plt.subplot(223)
# if args.logscale == 1:
# 	plt.semilogx(np.arange(len(Hx)),Hx)
# elif args.logscale == 0:
# 	plt.plot(Hx)
# plt.grid(True)

# plt.subplot(224)
# if args.logscale == 1:
# 	plt.semilogx(np.arange(len(Hy)),Hy)
# elif args.logscale == 0:
# 	plt.plot(Hy)
# plt.grid(True)

# plt.show()