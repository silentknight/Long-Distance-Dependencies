#!/usr/bin/env python

# System libs
import os
import argparse

# Installed libs
import matplotlib.pyplot as plt
import numpy as np

import data
import mutual_information as mi
import pointwise_mutual_information as pmi

def main():
	parser = argparse.ArgumentParser(description='Long Distance Dependency measurements')

	parser.add_argument('--data', type=str, default='dataset/dl4mt/', help='location of the data corpus')
	parser.add_argument('--words', type=int, default=0, help="Tokenize strings on words or characters: 1 = Words, 0 = Characters")

	parser.add_argument('--compute', type=str, default="mi", help="Type of computation chosen, Choose mi = Mutual Information, pmi = Pointwise Mutual Information")
	parser.add_argument('--log_type', type=str, default="log2", help="Choose Log Type, loge = Log to the base e, log2 = log to the base 2, log10 = log to the base 10")
	parser.add_argument('--threads', type=int, default=1, help='Number of threads to spawn')
	parser.add_argument('--datafilepath', type=str, default='ldd_data.dat', help='File path of last known data process path')
	parser.add_argument('--overlap', type=int, default=1, help="Allow overlaps between two independent substrings. 0 = No, 1 = Yes")
	parser.add_argument('--direction', type=str, default='bi', help="Random variables sampling direction, bi = Bidirectional, uni = Unidirectional")

	parser.add_argument('--clear', type=int, default=0, help="Clear old data file (ldd_data.dat)")

	parser.add_argument('--normalize', type=int, default=0, help="Normalize the scores in the range [0,1]")
	parser.add_argument('--plot_path', type=str, default='ldd_plot.png', help="Location of the plot to be saved")
	
	args = parser.parse_args()

	###############################################################################
	# Clear old data file
	###############################################################################

	if args.clear == 1:
		try:
			os.remove("ldd_data.dat")
		except OSError:
			print("ldd_data.dat file does not exist.")

	###############################################################################
	# Load data
	###############################################################################

	corpus = data.Corpus(args.data, args.words)

	##########################################################################################################################
	# Calculate Mutual Information or Pointwise Mutual Information
	##########################################################################################################################

	if args.compute == "mi":
		ldd = mi.MutualInformation(corpus, args.log_type, args.threads, args.datafilepath, args.overlap)
	elif args.compute == "pmi":
		p_ldd = pmi.PointwiseMutualInformation(args.log_type, args.threads, args.datafilepath, args.overlap)

	# #########################################################################################################################
	# # Plot the LDD
	# #########################################################################################################################

	if args.normalize == 1:
		x, Hx, Hy, Hxy = ldd.mutualInformation/np.amax(ldd.mutualInformation)
	else:
		x, Hx, Hy, Hxy = ldd.mutualInformation

	plt.subplot(221)
	plt.loglog(np.arange(len(x)),x,basex=10)
	plt.grid(True)

	plt.subplot(222)
	plt.semilogx(np.arange(len(Hxy)),Hxy)
	plt.grid(True)
	
	plt.subplot(223)
	plt.semilogx(np.arange(len(Hy)),Hy)
	plt.grid(True)

	plt.subplot(224)
	plt.semilogx(np.arange(len(Hx)),Hx)
	plt.grid(True)

	if(args.plot_path.split('.')[-1] == "png"):
		plot_filename = args.plot_path
	else:
		plot_filename = args.plot_path+".png"
	plt.savefig(plot_filename)
	plt.show()
	
	###############################################################################

if __name__ == '__main__':
		main()