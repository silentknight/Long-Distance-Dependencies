#!/usr/bin/env python

# System libs
import numpy as np
import argparse
import sys
import os
import ast
import scipy.sparse

parser = argparse.ArgumentParser(description='Get Contextual Dependencies')
parser.add_argument('--dataset', type=int, help='Dataset number as listed in LDD paper', required=True)
parser.add_argument('--start', type=int, default=1, help='Value of D (Dependency distance) from start for plotting. Default is 1')
parser.add_argument('--end', type=str, default='end', help='Value of D (Dependency distance) till end for plotting. Default is \'end\' (all the way will the end).')
parser.add_argument('--word', type=str, help='Word you want to find the distribution of', required=True)
args = parser.parse_args()

####################################################################################################
# Choose the dataset                                                                               #
####################################################################################################
def dataset_pick(i):
	switcher={
		1: '/mnt/data/pmi_data/penn_tree_words_standard_logx',
		2: '/mnt/data/pmi_data/text8_words_standard_logx',
		3: None,
		4: '/mnt/data/pmi_data/text8_subset_standard_logx',
		5: '/mnt/data/pmi_data/text8_subset_wor_standard_logx',
		6: '/mnt/data/pmi_data/wiki2_words_standard_logx',
		7: None,
		8: None,
		9: '/mnt/data/pmi_data/wiki103_words_standard_logx',
		10: None,
		11: None,
		12: '/mnt/data/pmi_data/wiki_sample_1_words_standard_logx',
		13: '/mnt/data/pmi_data/wiki_sample_2_words_standard_logx',
		14: '/mnt/data/pmi_data/wiki_sample_3_words_standard_logx',
		15: '/mnt/data/pmi_data/wiki_sample_4_words_standard_logx',
		16: None,
		17: '/mnt/data/pmi_data/wiki19_standard_logx',
		18: '/mnt/data/pmi_data/wiki19L_standard_logx',
		19: None,
		20: '/mnt/data/pmi_data/text8_subset_wor_4_standard_logx'
	}
	return switcher.get(i,"Invalid path")

path = dataset_pick(args.dataset)
print(path)

####################################################################################################
# Open the symbols file and check if the characters are present which are supplied in command line #
####################################################################################################
symbols = {}
try:
	f = open(path+"/0.symbols.dat", 'r')
	data = f.read()
	symbols = ast.literal_eval(data)
	f.close()
except:
	print(path+" does not exist. Please check the path. Do not add / at the end of the path.")
	sys.exit()

try:
	wordID = int(symbols[args.word])
	print("Word you supplied is: "+args.word+": "+str(wordID)+". Hence computing distribution across all other words.")
except:
	print("Either word is not supplied or it is not present in the dataset.")

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

fm = open("marginal_dependence_"+str(args.word)+"_"+str(args.dataset),"w")
d = start
try:
	for file in files:
		pmi_temp = scipy.sparse.load_npz(path+"/pmi/"+file)
		[pmi_rows, pmi_cols, pmi] = scipy.sparse.find(pmi_temp)
		temp1 = np.where(pmi_rows==wordID)[0]
		temp2 = np.where(pmi_cols==wordID)[0]
		index = np.concatenate((temp1,temp2))
		print(pmi[index])
		print(pmi_rows[index])
		print(pmi_cols[index])
		pmi = pmi[index]
		total = max(np.max(pmi_rows),np.max(pmi_cols))*2-1-index.shape[0]

		Ni_XY_temp = scipy.sparse.load_npz(path+"/Ni_XY/"+file)
		[Ni_XY_rows, Ni_XY_cols, Ni_XY] = scipy.sparse.find(Ni_XY_temp)
		Ni_XY = Ni_XY[index]

		pmi_data = np.load(path+"/np/"+file, mmap_mode='r', allow_pickle=True)
		Xi = pmi_data['arr_0']
		Yi = pmi_data['arr_1']
		Ni_X = pmi_data['arr_2'].tolist().toarray()[0]
		Ni_Y = pmi_data['arr_3'].tolist().toarray()[0]

		if args.dataset == 1:
			fm.write("%d," % np.size(pmi[np.where(pmi<-1.3)]))
			fm.write("%d," % np.size(pmi[np.where((pmi<0)&(pmi>=-1.3))]))
			fm.write("%d," % total)
			fm.write("%d," % np.size(pmi[np.where((pmi>0)&(pmi<=3))]))
			fm.write("%d," % np.size(pmi[np.where((pmi>3)&(pmi<=9.9))]))
			fm.write("%d," % np.size(pmi[np.where(pmi>9.9)]))
			fm.write("\n")
		elif args.dataset == 6:
			fm.write("%d," % np.size(pmi[np.where(pmi<-1.3)]))
			fm.write("%d," % np.size(pmi[np.where((pmi<0)&(pmi>=-1.3))]))
			fm.write("%d," % total)
			fm.write("%d," % np.size(pmi[np.where((pmi>0)&(pmi<=3.2))]))
			fm.write("%d," % np.size(pmi[np.where((pmi>3.2)&(pmi<=11.9))]))
			fm.write("%d," % np.size(pmi[np.where(pmi>11.9)]))
			fm.write("\n")
		elif args.dataset == 9:
			fm.write("%d," % np.size(pmi[np.where(pmi<-1.6)]))
			fm.write("%d," % np.size(pmi[np.where((pmi<0)&(pmi>=-1.6))]))
			fm.write("%d," % total)
			fm.write("%d," % np.size(pmi[np.where((pmi>0)&(pmi<=3))]))
			fm.write("%d," % np.size(pmi[np.where((pmi>3)&(pmi<=15.8))]))
			fm.write("%d," % np.size(pmi[np.where(pmi>15.8)]))
			fm.write("\n")
		elif args.dataset == 12:
			fm.write("%d," % np.size(pmi[np.where(pmi<-1.3)]))
			fm.write("%d," % np.size(pmi[np.where((pmi<0)&(pmi>=-1.3))]))
			fm.write("%d," % total)
			fm.write("%d," % np.size(pmi[np.where((pmi>0)&(pmi<=3.2))]))
			fm.write("%d," % np.size(pmi[np.where((pmi>3.2)&(pmi<=11.9))]))
			fm.write("%d," % np.size(pmi[np.where(pmi>11.9)]))
			fm.write("\n")
		elif args.dataset == 13:
			fm.write("%d," % np.size(pmi[np.where(pmi<-1.3)]))
			fm.write("%d," % np.size(pmi[np.where((pmi<0)&(pmi>=-1.3))]))
			fm.write("%d," % total)
			fm.write("%d," % np.size(pmi[np.where((pmi>0)&(pmi<=3.2))]))
			fm.write("%d," % np.size(pmi[np.where((pmi>3.2)&(pmi<=11.9))]))
			fm.write("%d," % np.size(pmi[np.where(pmi>11.9)]))
			fm.write("\n")
		elif args.dataset == 14:
			fm.write("%d," % np.size(pmi[np.where(pmi<-1.3)]))
			fm.write("%d," % np.size(pmi[np.where((pmi<0)&(pmi>=-1.3))]))
			fm.write("%d," % total)
			fm.write("%d," % np.size(pmi[np.where((pmi>0)&(pmi<=3.2))]))
			fm.write("%d," % np.size(pmi[np.where((pmi>3.2)&(pmi<=11.9))]))
			fm.write("%d," % np.size(pmi[np.where(pmi>11.9)]))
			fm.write("\n")
		elif args.dataset == 15:
			fm.write("%d," % np.size(pmi[np.where(pmi<-1.3)]))
			fm.write("%d," % np.size(pmi[np.where((pmi<0)&(pmi>=-1.3))]))
			fm.write("%d," % total)
			fm.write("%d," % np.size(pmi[np.where((pmi>0)&(pmi<=3.2))]))
			fm.write("%d," % np.size(pmi[np.where((pmi>3.2)&(pmi<=11.9))]))
			fm.write("%d," % np.size(pmi[np.where(pmi>11.9)]))
			fm.write("\n")
		else:
			print("Dataset not available")
			exit()

		print("Processed -> d: %d" % d)

		if end == "end":
			pass
		elif d == end:
			exit()

		d+=1

except (KeyboardInterrupt, ValueError) as e:
	print(e)
	print("Processing halted. Printing upto d: "+str(d-1))

fm.close()
