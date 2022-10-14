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
parser.add_argument('--dataset', type=int, default=1, help='Dataset number as listed in LDD paper')
parser.add_argument('--start', type=int, default=1, help='Value of D (Dependency distance) from start for plotting. Default is 1')
parser.add_argument('--end', type=str, default='end', help='Value of D (Dependency distance) till end for plotting. Default is \'end\' (all the way will the end).')
parser.add_argument('--logscale', type=int, default=1, help='Plot on Log Scale or normal scale. 1: Log Scale; 0: Normal Scale')
parser.add_argument('--normalize', type=str, default='n', help='Normalize values')
parser.add_argument('--word1', type=str, help='Word you want to find the distribution of', required=True)
parser.add_argument('--word2', type=str, help='Word against which you want to find the distribution')
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
try:
	word1 = -1
	word2 = -1

	f = open(path+"/0.symbols.dat", 'r')
	data = f.read()
	symbols = ast.literal_eval(data)

	if args.word1 in symbols and args.word2 in symbols:
		wordID_1 = int(symbols[args.word1])
		wordID_2 = int(symbols[args.word2])
		print("Words you supplied were found:\n"+args.word1+": "+str(wordID_1)+" and "+args.word2+": "+str(wordID_2))
	elif args.word2 == None:
		wordID_1 = int(symbols[args.word1])
		print("Word you supplied is: "+args.word1+": "+str(wordID_1)+". Hence computing distribution across all other words.")
	else:
		print("Words you supplied were not present in the dataset. Hence Exiting !!")
		sys.exit()
	f.close()
except:
	print(path+" does not exist. Please check the path. Do not add / at the end of the path.")
	sys.exit()

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

print("Pull data from numpy file")

d = start
pmi_single = np.empty((0,1))
Ni_XY_single = np.empty((0,1))
pmi_row = []
Ni_XY_row = []

for file in files:
	pmi_data = np.load(path+"/np/"+file, mmap_mode='r', allow_pickle=True)
	Xi = pmi_data['arr_0']
	Yi = pmi_data['arr_1']
	Ni_X = pmi_data['arr_2']
	Ni_Y = pmi_data['arr_3']
	Ni_XY = scipy.sparse.load_npz(path+"/Ni_XY/"+file)
	pmi = scipy.sparse.load_npz(path+"/pmi/"+file)

	if args.word2 == None:
		if pmi_row == []:
			pmi_row = pmi[np.where(Xi==wordID_1)[0][0],:].toarray()
			Ni_XY_row = Ni_XY[np.where(Xi==wordID_1)[0][0],:].toarray()
		else:
			pmi_row = np.append(pmi_row, pmi[np.where(Xi==wordID_1)[0][0],:].toarray(), axis=0)
			Ni_XY_row = np.append(Ni_XY_row, Ni_XY[np.where(Xi==wordID_1)[0][0],:].toarray(), axis=0)
	else:
		pmi_single = np.append(pmi_single, pmi[np.where(Xi==wordID_1)[0][0],np.where(Yi==wordID_2)[0][0]])
		Ni_XY_single = np.append(Ni_XY_single, Ni_XY[np.where(Xi==wordID_1)[0][0],np.where(Yi==wordID_2)[0][0]])

	sys.stdout.write("\rProcessed -> d: %d" % (d))
	sys.stdout.flush()
	d += 1

if args.word2 == None:
	print("\nJust one word selected...")
	#np.set_printoptions(threshold=sys.maxsize, formatter={'float': lambda x: "{0:0.3f}".format(x)})
	#print(np.nonzero(pmi_row[0]))
	fig = plt.figure()
	ax = plt.axes()
#	ax = fig.add_subplot(211)
	plt.imshow(np.transpose(pmi_row))
	ax.set_aspect('auto')
	ax.xaxis.set_major_locator(MaxNLocator(integer=True))
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.colorbar(orientation='vertical')
#	ax = fig.add_subplot(212)
#	plt.imshow(np.transpose(Ni_XY_row))
#	ax.set_aspect('auto')
#	ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
#	plt.colorbar(orientation='vertical')
	print("Maximum frequency: %d" % (np.max(Ni_XY_row)))
	plt.savefig("pmi_word_"+args.word1+"_"+str(args.dataset))
	plt.show()
else:
	print("Two words selected...")
	print(Ni_XY_single.max())
	plt.subplot(211)
	if args.logscale == 1:
		plt.loglog(np.arange(len(pmi_single)),pmi_single,basex=10)
	elif args.logscale == 0:
		plt.plot(pmi_single)
	plt.grid(True)
	plt.subplot(212)
	if args.logscale == 1:
		plt.loglog(np.arange(len(Ni_XY_single)),Ni_XY_single,basex=10)
	elif args.logscale == 0:
		plt.bar(np.arange(len(pmi_single)),Ni_XY_single)
	plt.grid(True)
	plt.show()
