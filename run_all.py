#!/usr/bin/env python

# System libs
import os
import argparse

# Installed libs
import matplotlib.pyplot as plt
import numpy as np

import data
import mutual_information as mi

def main():
	parser = argparse.ArgumentParser(description='Long Distance Dependency measurements')
	parser.add_argument('--data', type=str, default='dataset/dl4mt/', help='location of the data corpus')
	parser.add_argument('--method', type=str, default="MI", help="Type of method chosen, Choose mi=Relative Entropy, copula=Copulas")
	parser.add_argument('--log_type', type=str, default="loge", help="Choose Log Type, loge=Log to the base e, log2=log to the base 2, log10=log to the base 10")
	parser.add_argument('--threads', type=int, default=1, help='Number of threads to spawn')
	parser.add_argument('--datafilepath', type=str, default='ldd_data.dat', help='File path of last known data process path')
	parser.add_argument('--clear', type=int, default=0, help="Clear old data file (ldd_data.dat)")
	parser.add_argument('--overlap', type=int, default=1, help="Allow overlaps between two independent substrings. 0-No, 1-Yes")
	parser.add_argument('--normalize', type=int, default=0, help="Normalize the scores in the range [0,1].")
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

	concatenate = False
	if args.overlap == 1:
		concatenate = True
	corpus = data.Corpus(args.data, concatenate)

	###############################################################################
	# Calculate Mutual Information
	###############################################################################

	ldd = mi.MutualInformation(corpus, args.threads, args.datafilepath, args.overlap)

	# ###############################################################################
	# # Plot the LDD
	# ###############################################################################

	if args.normalize == 1:
		x, Hx, Hy, Hxy = ldd.mutualInformation/np.amax(ldd.mutualInformation)
	else:
		x, Hx, Hy, Hxy = ldd.mutualInformation

	plt.subplot(161)
	plt.semilogy(np.arange(len(x)),x)
	plt.subplot(162)
	plt.plot(np.arange(len(x)),x)
	plt.subplot(163)
	plt.plot(np.arange(len(Hx)),Hx)
	plt.subplot(164)
	plt.plot(np.arange(len(Hy)),Hy)
	plt.subplot(165)
	plt.plot(np.arange(len(Hx)),Hx+Hy)
	plt.subplot(166)
	plt.plot(np.arange(len(Hxy)),Hxy)
	plt.show()
	
	###############################################################################

if __name__ == '__main__':
		main()