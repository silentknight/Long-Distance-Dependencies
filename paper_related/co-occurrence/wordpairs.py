#!/usr/bin/env python

# System libs
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import LogNorm
import numpy as np
import argparse
import sys
import os
import re
import ast
import scipy.sparse

parser = argparse.ArgumentParser(description='Get Contextual Dependencies')
parser.add_argument('--dataset', type=int, help='Dataset number as listed in LDD paper', required=True)
parser.add_argument('--start', type=int, default=1, help='Value of D (Dependency distance) from start for plotting. Default is 1')
parser.add_argument('--end', type=str, default='end', help='Value of D (Dependency distance) till end for plotting. Default is \'end\' (all the way will the end).')
parser.add_argument('--logscale', type=int, default=1, help='Plot on Log Scale or normal scale. 1: Log Scale; 0: Normal Scale')
parser.add_argument('--normalize', type=str, default='n', help='Normalize values')
parser.add_argument('--word1', type=str, help='Word you want to find the distribution of')
parser.add_argument('--word2', type=str, help='Word against which you want to find the distribution')
parser.add_argument('--pmi_l', type=float, help='PMI lower threshold')
parser.add_argument('--pmi_u', type=float, help='PMI upper threshold')
args = parser.parse_args()

####################################################################################################
# Choose the dataset                                                                               #
####################################################################################################
def dataset_pick(i):
	switcher={
		1: '/mnt/data/pmi_data/penn_tree_words_standard_logx',
		2: '/mnt/data/pmi_data/text8_words_standard_logx',
		3: None,
		4: None,
		5: None,
		6: '/mnt/data/pmi_data/wiki2_words_standard_logx',
		7: None,
		8: '/mnt/data/pmi_data/wiki103_words_standard_logx',
		9: None,
		10: '/mnt/data/pmi_data/wiki_sample_3_words_standard_logx',
		11: '/mnt/data/pmi_data/wiki_sample_4_words_standard_logx',
		12: None
	}
	return switcher.get(i,"Invalid path")

path = dataset_pick(args.dataset)
print(path)

####################################################################################################
# Open the symbols file and check if the characters are present which are supplied in command line #
####################################################################################################
symbols = {}
try:
	word1 = -1
	word2 = -1

	f = open(path+"/0.symbols.dat", 'r')
	data = f.read()
	symbols = ast.literal_eval(data)

	f.close()
except:
	print(path+" does not exist. Please check the path. Do not add / at the end of the path.")
	sys.exit()

try:
	if args.word1 in symbols and args.word2 in symbols:
		wordID_1 = int(symbols[args.word1])
		wordID_2 = int(symbols[args.word2])
		print("Words you supplied were found:\n"+args.word1+": "+str(wordID_1)+" and "+args.word2+": "+str(wordID_2))
	elif args.word2 == None:
		wordID_1 = int(symbols[args.word1])
		print("Word you supplied is: "+args.word1+". Hence computing distribution across all other words.")
except:
	print("Either words are not supplied or supplied words are not present in the dataset.")

####################################################################################################
# Get the start and end of "d"                                                                     #
####################################################################################################
start = 1
end = 0

if args.start > 0:
	start = args.start
else:
	print("Start value cannot be less that 1 as Distance cannot be less than 1")
	sys.exit()

try:
	end = int(args.end)
except ValueError:
	if args.end == "end":
		pass
	else:
		print("Not a well formed integer")
		sys.exit()

####################################################################################################
# Get the data from the files                                                                      #
####################################################################################################
print("Pulling file list from the folder")

try:
	d_num = []
	ext = ""
	files = sorted(os.listdir(path+"/pmi"))
	for file in files:
		d_num.append(int(file.split('.')[0]))
		ext = file.split('.')[1]

	d_num = sorted(d_num)
	files = []
	for file in d_num:
		if args.end == "end":
			if file >= start:
				files.append(str(file)+'.'+ext)
		else:
			if file >= start and file <= end:
				files.append(str(file)+'.'+ext)
except:
	print(path+" does not exist")

print("Pull data from numpy file")

d = start
try:
	for file in files:
		pmi_temp = scipy.sparse.load_npz(path+"/pmi/"+file)
		[pmi_rows, pmi_cols, pmi] = scipy.sparse.find(pmi_temp)

		Ni_XY_temp = scipy.sparse.load_npz(path+"/Ni_XY/"+file)
		[Ni_XY_rows, Ni_XY_cols, Ni_XY] = scipy.sparse.find(Ni_XY_temp)

		pmi_data = np.load(path+"/np/"+file, mmap_mode='r', allow_pickle=True)
		Xi = pmi_data['arr_0']
		Yi = pmi_data['arr_1']
		Ni_X = pmi_data['arr_2'].tolist().toarray()[0]
		Ni_Y = pmi_data['arr_3'].tolist().toarray()[0]

		if args.pmi_l != None and args.pmi_u != None:
			index = np.where((pmi>=args.pmi_l)&(pmi<=args.pmi_u))
		elif args.pmi_l == None:
			index = np.where(pmi<=args.pmi_u)
		elif args.pmi_u == None:
			index = np.where(pmi>=args.pmi_l)
		else:
			print("No PMI thresholds provided")
			exit()

		for i in index[0]:
			found_word1 = ""
			found_word2 = ""
			for word, wordID in symbols.items():
				if pmi_rows[i] == wordID:
					found_word1 = word
				if pmi_cols[i] == wordID:
					found_word2 = word

			if(Ni_X[pmi_rows[i]]>5 and Ni_Y[pmi_cols[i]]>5 and Ni_XY[i]>1 and (found_word1==args.word1 or found_word2==args.word1)):
				print("%s (%d) & %s (%d) & %d & %3.5f" %(found_word1, Ni_X[pmi_rows[i]], found_word2, Ni_Y[pmi_cols[i]], Ni_XY[i], pmi[i]))

		print("Processed -> d: %d" % d)

		if end == "end":
			pass
		elif d == end:
			exit()

		d+=1

except (KeyboardInterrupt, ValueError) as e:
	print(e)
	print("Processing halted. Printing upto d: "+str(d-1))
