#!/usr/bin/env python

# System libs
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser(description="Long Distance Dependency measurements plot")
parser.add_argument('--path', type=str, required=True, help="Path of the data file.")
parser.add_argument('--start', type=int, default=1, help="Start plotting from d. Default is 1.")
parser.add_argument('--end', type=int, help="End plotting till d.")
parser.add_argument('--loglog', type=int, default=1, help="Plot on Log-Log Scale or Linear scale. 1: Log-Log Scale; 0: Normal Scale")
parser.add_argument('--save', type=str, default="ldd", help="Path to save the plot (no extensions)")
args = parser.parse_args()
	
try:
	f = open(args.path, "r")
	lines = f.readlines()
	f.close()
except FileNotFoundError:
	print("Filename %s does not exist." % args.path)
	sys.exit()

start = 0
if args.start > 0:
	start = args.start
else:
	print("Start value cannot be less that 1 as Distance cannot be less than 1")
	sys.exit()

end = 0
if args.end:
	end = int(args.end)
else:
	end = len(lines)

mi = np.zeros([0,1])
Hx = np.zeros([0,1])
Hy = np.zeros([0,1])
Hxy = np.zeros([0,1])
temp = lines[0].split()
index = 0

if temp[0] == "data:":
	for line in lines:
		temp = line.strip().split(":")
		if temp[0] == "d":
			temp1 = temp[2].split(",")				
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
	print("Not a valid file")

mi = mi[start-1:end]
Hx = Hx[start-1:end]
Hy = Hy[start-1:end]
Hxy = Hxy[start-1:end]

with plt.style.context(('seaborn')):
	fig, axes = plt.subplots(2, 2)

	if args.loglog == 1:
		axes[0,0].loglog(np.arange(1, len(mi)+1), mi, label="Dependency Decay Curve")
		axes[0,1].semilogx(np.arange(1, len(Hxy)+1), Hxy, label="Joint Entropy")
		axes[1,0].semilogx(np.arange(1, len(Hx)+1), Hx, label="Entropy of X")
		axes[1,1].semilogx(np.arange(1, len(Hy)+1), Hy, label="Entropy of Y")
	elif args.loglog == 0:
		axes[0,0].plot(np.arange(1, len(mi)+1), mi, label="Dependency Decay Curve")
		axes[0,1].semilogx(np.arange(1, len(Hxy)+1), Hxy, label="Joint Entropy")
		axes[1,0].semilogx(np.arange(1, len(Hx)+1), Hx, label="Entropy of X")
		axes[1,1].semilogx(np.arange(1, len(Hy)+1), Hy, label="Entropy of Y")

	axes[0,0].grid(True)
	axes[0,0].axes.xaxis.set_ticklabels([])
	axes[0,0].tick_params(labelsize='small', width=3)
	axes[0,0].grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	axes[0,0].grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	axes[0,0].set_xlim(1, len(mi)+1)
	axes[0,0].set_ylim(0.9, 3)
	# axes[0,0].set_xlabel('Distance between words, d', fontsize=10)
	axes[0,0].set_ylabel('Mutual Information, I(d)', fontsize=10)
	lgd = axes[0,0].legend(loc='upper right', shadow=True, fancybox=True, ncol=1, numpoints=1, prop={'size': 10})

	axes[0,1].grid(True)
	axes[0,1].axes.xaxis.set_ticklabels([])
	axes[0,1].yaxis.set_label_position("right")
	axes[0,1].yaxis.tick_right()
	axes[0,1].tick_params(labelsize='small', width=3)
	axes[0,1].grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	axes[0,1].grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	axes[0,1].set_xlim(1, len(Hxy)+1)
	axes[0,1].set_ylim(11.6, 14.1)
	# axes[0,1].set_xlabel('Distance between words, d', fontsize=10)
	axes[0,1].set_ylabel('Entropy', fontsize=10)
	lgd = axes[0,1].legend(loc='lower right', shadow=True, fancybox=True, ncol=1, numpoints=1, prop={'size': 10})

	axes[1,0].grid(True)
	axes[1,0].tick_params(labelsize='small', width=3)
	axes[1,0].grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	axes[1,0].grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	axes[1,0].set_xlim(1, len(Hx)+1)
	# axes[1,0].set_ylim(2.2, 6.9)
	axes[1,0].set_xlabel('Distance between words, d', fontsize=10)
	axes[1,0].set_ylabel('Entropy', fontsize=10)
	lgd = axes[1,0].legend(loc='upper left', shadow=True, fancybox=True, ncol=1, numpoints=1, prop={'size': 10})

	axes[1,1].grid(True)
	axes[1,1].yaxis.set_label_position("right")
	axes[1,1].yaxis.tick_right()
	axes[1,1].tick_params(labelsize='small', width=3)
	axes[1,1].grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	axes[1,1].grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	axes[1,1].set_xlim(1, len(Hy)+1)
	# axes[1,1].set_ylim(6.9, 7.6)
	axes[1,1].set_xlabel('Distance between words, d', fontsize=10)
	axes[1,1].set_ylabel('Entropy', fontsize=10)
	lgd = axes[1,1].legend(loc='lower left', shadow=True, fancybox=True, ncol=1, numpoints=1, prop={'size': 10})

	fig.suptitle(args.path)
	plt.show()
	if args.save:
		fig.savefig(args.save+'.png', bbox_extra_artists=(lgd,), bbox_inches='tight')