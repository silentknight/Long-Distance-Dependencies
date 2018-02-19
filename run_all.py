#!/usr/bin/python3

import os
import time

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

if __name__ == '__main__':
	main()