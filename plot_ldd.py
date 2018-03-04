#!/usr/bin/env python

# System libs
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser(description='Long Distance Dependency measurements plot')
parser.add_argument('--path', type=str, default='ldd_data.dat', help='path of the data file')
parser.add_argument('--start', type=int, default=1, help='Value of D (Dependency distance) from start for plotting. Default is 1')
parser.add_argument('--end', type=str, default='end', help='Value of D (Dependency distance) till end for plotting. Default is \'end\' (all the way will the end).')
parser.add_argument('--normalize', type=str, default='n', help='normalize values')
args = parser.parse_args()
	
try:
	f = open(args.path, "r")
	lines = f.readlines()
	f.close()
except FileNotFoundError:
	print("No such file exists. Default file is ldd_data.dat")
	sys.exit()

start = 0
end = 0
index = 0

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

mi = np.zeros([0,1])
temp = lines[0].split()
if temp[0] == "data:":
	for line in lines:
		temp = line.strip().split(":")
		if start<=index and end>=index:
			if temp[0] == "d":
				mi = np.append(mi,np.zeros(1))
				mi[int(temp[1])-start] = float(temp[2])
				d = int(temp[1])+1
		index+=1
else:
	print("Not a valid file")

if args.normalize == "y" or args.normalize == "Y":
	x = mi/np.amax(mi)
else:
	x = mi

plt.subplot(121)
plt.semilogy(np.arange(start,end+1),x)
plt.subplot(122)
plt.plot(np.arange(start,end+1),x)
plt.show()