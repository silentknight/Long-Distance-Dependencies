import os
import numpy as np

filename = "penn_tree_words_full_grassberger_logx_mi.dat"

d = 1

if(os.path.exists(filename)):
	f = open(filename,"r")
	lines = f.readlines()
	f.close()

	mi = np.zeros([len(lines)-1])
	Hx = np.zeros([len(lines)-1])
	Hy = np.zeros([len(lines)-1])
	Hxy = np.zeros([len(lines)-1])

	temp = lines[0].split()
	if temp[0] == "data:" and temp[1] == "dataset/dl4mt/":
		for line in lines:
			temp = line.strip().split(":")
			if temp[0] == "d":
				temp1 = temp[2].split(",")
				mi[int(temp[1])-1] = float(temp1[0])
				Hx[int(temp[1])-1] = float(temp1[1])
				Hy[int(temp[1])-1] = float(temp1[2])
				Hxy[int(temp[1])-1] = float(temp1[3])
				d = int(temp[1])+1
				print(d)
else:
	print("File does not exist to load previous data")


print(mi)