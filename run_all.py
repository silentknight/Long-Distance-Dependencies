#!/usr/bin/env python

# System libs
from collections import OrderedDict
import os
import sys
import shutil
import gzip
import pickle
import copy
import argparse
import time

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
	parser.add_argument('--threads', type=int, default='4', help='Number of threads to spawn')
	parser.add_argument('--datafilepath', type=str, default='ldd_data.dat', help='File path of last known data process path')
	args = parser.parse_args()

	###############################################################################
	# Load data
	###############################################################################

	corpus = data.Corpus(args.data)

	###############################################################################
	# Calculate Mutual Information
	###############################################################################

	ldd = mi.MutualInformation(corpus, args.threads, args.datafilepath)

	###############################################################################
	# Plot the LDD
	###############################################################################

	# x = ldd.mutualInformation/np.amax(ldd.mutualInformation)
	x = ldd.mutualInformation
	plt.subplot(121)
	plt.semilogy(np.arange(len(x)),x)
	plt.subplot(122)
	plt.plot(np.arange(len(x)),x)
	plt.show()
	
	###############################################################################

if __name__ == '__main__':
	main()