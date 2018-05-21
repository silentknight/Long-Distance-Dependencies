#!/usr/bin/env python

# System libs
import os
import argparse

# Installed libs
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns

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
	parser.add_argument('--words', type=int, default=0, help="Tokenize strings on words or characters: 1-Words, 0-Characters.")
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

	with sns.axes_style("white"):
		sns.set_style("ticks")
		sns.set_context("talk")


		#plt.subplot(221)
		plt.loglog(np.arange(len(x)),x,basex=10, color='k')
		plt.xlabel('Distance between symbols d(X,Y)', fontsize=20)
		plt.ylabel('Mutual Information I(X,Y) in bits', fontsize=20)
		plt.tight_layout()
		plt.tick_params(labelsize=20)
		sns.despine()
		plt.tight_layout()
		plt.grid(True)

		#plt.subplot(222)
		#plt.semilogx(np.arange(len(Hxy)),Hxy)
		#plt.grid(True)

		#plt.subplot(223)
		#plt.semilogx(np.arange(len(Hy)),Hy)
		#plt.grid(True)

		#plt.subplot(224)
		#plt.semilogx(np.arange(len(Hx)),Hx)
		#plt.grid(True)

		plt.show()
	
	###############################################################################

if __name__ == '__main__':
		main()