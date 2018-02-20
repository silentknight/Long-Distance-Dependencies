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

# Setup matplotlib renderer to avoid using the screen (must be done early)
import matplotlib
matplotlib.use('Agg')

# Installed libs
import matplotlib.pyplot as plt
import numpy as np

import data
import mutual_information as mi

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


def pmi_Penn_Tree_Bank_data():
	data_Dir = "dataset/penn-tree-bank/treebank/raw"

	sequential_Data = ""

	for root, dirs, files in os.walk(data_Dir):
		for fname in sorted(files):
			file_Name = os.path.join(root, fname)

			data_File = open(file_Name, "r")
			lines = data_File.readlines()
			data_File.close()

			valid_File = False
			for line in lines:
				if line.strip() == ".START":
					valid_File = True
				else:
					if valid_File == True:
						sequential_Data += line.strip()

	print(sequential_Data)
	print(len(sequential_Data))

def pmi_SP_Data():
	data_Dir_Original = "dataset/foma/Original_Data"
	data_Dir_Generated = "dataste/foma/Generated_Data"

	for root, dirs, files in os.walk(data_Dir_Original):
		for fname in sorted(files):
			file_Name = os.path.join(root, fname)
			# print(file_Name)


def pmi_wikiText2_Data():
	pass
	

def pmi_wikiText103_Data():
	pass

def main():
	pmi_Penn_Tree_Bank_data()
	pmi_SP_Data()
	pmi_wikiText2_Data()
	pmi_wikiText103_Data()

# if __name__ == '__main__':
# 	main()