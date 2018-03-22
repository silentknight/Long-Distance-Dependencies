#!/usr/bin/env python

# System libs
import numpy as np
import scipy.special as spec
import sys
import threading
import os
import time

class myThread(threading.Thread):
	def __init__(self, d, overlap):
		self.d = d
		self.mi = 0
		self.Hx = 0
		self.Hy = 0
		self.Hxy = 0
		self.overlap = overlap
		super(myThread, self).__init__()

	def run(self):
		if self.overlap == 1:
			X = [item for sublist in corpus.sequentialData.wordArray for item in sublist]
			X_new = np.array(X)
			steps = int(X_new.size/self.d)
			last = steps*self.d
			Y_new = X_new[self.d:last]
			X_new = X_new[0:last-self.d]
		elif self.overlap == 0:
			X = []
			Y = []
			for line in corpus.sequentialData.wordArray:
				steps = int(len(line)/self.d)
				last = steps*self.d
				X = X+line[0:last-self.d]
				Y = Y+line[self.d:last]
			X_new = np.array(X)
			Y_new = np.array(Y)

		unique_X, counts_X = np.unique(X_new, return_counts=True)
		unique_Y, counts_Y = np.unique(Y_new, return_counts=True)

		XY = np.zeros((unique_X.size,unique_Y.size))
		for index in range(X_new.size):
			XY[np.where(unique_X==X_new[index])[0][0],np.where(unique_Y==Y_new[index])[0][0]]+=1

		self.Hx = np.log(np.sum(counts_X))-np.sum(counts_X*spec.digamma(counts_X))/np.sum(counts_X)
		self.Hy = np.log(np.sum(counts_Y))-np.sum(counts_Y*spec.digamma(counts_Y))/np.sum(counts_Y)
		XY = XY.reshape(counts_X.size*counts_Y.size)
		XY = np.delete(XY,np.where(XY==0)[0])
		self.Hxy = np.log(np.sum(XY))-np.sum(XY*spec.digamma(XY))/np.sum(XY)

		self.mi = self.Hx+self.Hy-self.Hxy

class MutualInformation(object):
	def __init__(self, corpusData, no_of_threads, data_file_path, overlap):
		global corpus
		corpus = corpusData
		self.no_of_threads = no_of_threads
		self.filename = data_file_path
		self.overlap = overlap
		self.mutualInformation = self.calculate_MI()

	def calculate_MI(self):
		mi = np.zeros([0,1])
		Hx = np.zeros([0,1])
		Hy = np.zeros([0,1])
		Hxy = np.zeros([0,1])
		d = 1

		# Check if already processing is done or new process ?
		if(os.path.exists(self.filename)):
			f = open(self.filename,"r")
			lines = f.readlines()
			f.close()

			temp = lines[0].split()
			if temp[0] == "data:" and temp[1] == corpus.datainfo:				
				for line in lines:
					temp = line.strip().split(":")
					if temp[0] == "d":
						temp1 = temp[2].split(",")
						mi = np.append(mi,np.zeros(1))
						mi[int(temp[1])-1] = float(temp1[0])
						Hx = np.append(Hx,np.zeros(1))
						Hx[int(temp[1])-1] = float(temp1[1])
						Hy = np.append(Hy,np.zeros(1))
						Hy[int(temp[1])-1] = float(temp1[2])
						Hxy = np.append(Hxy,np.zeros(1))
						Hxy[int(temp[1])-1] = float(temp1[3])
						d = int(temp[1])+1

		end = False
		try:
			max_distance = corpus.sequentialData.wordCount
			while d<max_distance and end==False:
				mi = np.append(mi,np.zeros(self.no_of_threads))
				Hx = np.append(Hx,np.zeros(self.no_of_threads))
				Hy = np.append(Hy,np.zeros(self.no_of_threads))
				Hxy = np.append(Hxy,np.zeros(self.no_of_threads))

				thread = []
				for i in range(self.no_of_threads):
					thread.append(myThread(d+i, self.overlap))

				for i in range(self.no_of_threads):
					thread[i].start()

				for i in range(self.no_of_threads):
					thread[i].join()

				for i in range(self.no_of_threads):
					mi[d+i-1] = thread[i].mi
					Hx[d+i-1] = thread[i].Hx
					Hy[d+i-1] = thread[i].Hy
					Hxy[d+i-1] = thread[i].Hxy
					print(thread[i].d, thread[i].mi, thread[i].Hx, thread[i].Hy, thread[i].Hx+thread[i].Hy, thread[i].Hxy)
				
				d += self.no_of_threads
		except KeyboardInterrupt:
			for i in range(self.no_of_threads):
				if mi[len(mi)-1]==0:
					mi = np.delete(mi,len(mi)-1)
					Hx = np.delete(Hx,len(Hx)-1)
					Hy = np.delete(Hy,len(Hy)-1)
					Hxy = np.delete(Hxy,len(Hxy)-1)

		f = open(self.filename,"w")
		f.write("data: "+corpus.datainfo+"\n")
		for i in range(len(mi)):
			f.write("d:"+str(i+1)+":"+str(mi[i])+","+str(Hx[i])+","+str(Hy[i])+","+str(Hxy[i])+"\n")
		f.close()

		return mi, Hy, Hy, Hxy