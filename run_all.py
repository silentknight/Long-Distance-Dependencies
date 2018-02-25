#!/usr/bin/env python

# System libs
from __future__ import print_function
if hasattr(__builtins__, 'raw_input'):
    input = raw_input

from collections import OrderedDict
import os
import sys
import shutil
import gzip
import pickle
import copy
import argparse
import time

# Setup matplotlib renderer to avoid using the screen (must be done early)
import matplotlib
matplotlib.use('Agg')

# Installed libs
import matplotlib.pyplot as plt
import numpy as np

import data
import mutual_information as mi

def main():
	parser = argparse.ArgumentParser(description='Long Distance Dependency measurements')
	parser.add_argument('--data', type=str, default='dataset/dl4mt/', help='location of the data corpus')
	parser.add_argument('--model', type=str, default='LSTM', help='type of recurrent net (LSTM, QRNN, GRU)')
	args = parser.parse_args()

	###############################################################################
	# Load data
	###############################################################################

	corpus = data.Corpus(args.data)

	###############################################################################
	# Calculate Mutual Information
	###############################################################################

	ldd = mi.MutualInformation(corpus)

	###############################################################################
	# Plot the LDD
	###############################################################################

	###############################################################################
	# Calculate the measure of LDD
	###############################################################################


if __name__ == '__main__':
	main()