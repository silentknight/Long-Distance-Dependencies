#!/usr/bin/env python

# System libs
import os
import argparse
import shutil
import time

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
	parser.add_argument('--cutoff', type=int, help="Value of maximum D you need.", required=True)
	parser.add_argument('--compute', type=str, default="mi", help="Type of computation chosen, Choose mi = Mutual Information, pmi = Pointwise Mutual Information")
	parser.add_argument('--mi_method', type=str, default="grassberger", help="MI calculation method, Choose standard = Standard Calculation, grassberger = Grassberger adjustments")
	parser.add_argument('--pmi_method', type=str, default="standard", help="PMI calculation method, Choose standard = Standard Calculation, pmi = Pointwise Mutual Information")
	parser.add_argument('--log_type', type=int, default=1, help="Choose Log Type, 0 = Log to the base e, 1 = log to the base 2, 2 = log to the base 10")
	parser.add_argument('--threads', type=int, default=1, help='Number of threads to spawn')
	parser.add_argument('--top_dir', type=str, default='', help='To change directory, add path of your preferred directory. Default: current working directory')
	parser.add_argument('--datafilepath', type=str, default='log_data', help='File name to store log data and load already stored files. Default filenames:- MI: log_data_mi.dat, PMI: log_data_pmi.dat')
	parser.add_argument('--overlap', type=int, default=1, help="Allow overlaps between two independent substrings. 0 = No, 1 = Yes")
	parser.add_argument('--direction', type=str, default='bi', help="Random variables sampling direction, bi = Bidirectional, uni = Unidirectional")

	parser.add_argument('--clear', type=int, default=0, help="Clear old data file")

	parser.add_argument('--normalize', type=int, default=0, help="Normalize the scores in the range [0,1]")
	parser.add_argument('--plot_path', type=str, default='ldd_plot.png', help="Location of the plot to be saved")

	args = parser.parse_args()

	###############################################################################
	# Load data
	###############################################################################

	corpus = data.Corpus(args.data, args.words)

	##########################################################################################################################
	# Calculate Mutual Information or Pointwise Mutual Information
	##########################################################################################################################

	if args.compute == "mi":
		args.datafilepath += "_mi.dat"
		if args.clear == 1:
			try:
				os.remove(args.datafilepath)
			except OSError:
				print(args.datafilepath+" file does not exist.")
		ldd = mi.MutualInformation(corpus, args.log_type, args.threads, args.datafilepath, args.overlap, args.mi_method, args.cutoff)

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

	elif args.compute == "pmi":
		if args.top_dir != '' and args.top_dir[len(args.top_dir)-1] != '/':
			args.top_dir += '/'

		if not os.path.exists(args.top_dir+"pmi_data"):
			os.makedirs(args.top_dir+"pmi_data")

		args.datafilepath = args.top_dir+"pmi_data/"+args.datafilepath

		if args.clear == 1:
			try:
				shutil.rmtree(args.datafilepath)
			except OSError:
				print("Cannot remove. "+args.datafilepath+" path does not exist.")

		if not os.path.isdir(args.datafilepath):
			os.mkdir(args.datafilepath);

		p_ldd = pmi.PointwiseMutualInformation(corpus, args.log_type, args.threads, args.datafilepath, args.overlap, args.pmi_method, args.cutoff)

	###############################################################################

if __name__ == '__main__':
		main()
