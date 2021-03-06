#!/usr/bin/env python

# System libs
import numpy as np
import scipy.special as spec
import sys
import threading
import os
import lddCalc
import array
import scipy.sparse

class myThread(threading.Thread):
	def __init__(self, d, overlap, log_type, method):
		self.d = d
		self.mi = 0
		self.Hx = 0
		self.Hy = 0
		self.Hxy = 0
		self.complete = False
		self.overlap = overlap
		self.method = method
		self.log_type = log_type
		super(myThread, self).__init__()

	def run(self):
		Ni_X, Ni_Y, Ni_XY, u_X, u_Y = lddCalc.getJointRV(dataArray, lineLengthList, totalLength, self.d, self.overlap)

		try:
			if Ni_X.nnz == 0 and Ni_Y.nnz == 0 and Ni_XY.nnz == 0:
				self.complete = True
				exit()
		except ValueError:
			pass


		log = lambda val,base: np.log(val) if base==0 else np.log2(val)

		Ni_X = Ni_X.data
		Ni_Y = Ni_Y.data
		Ni_XY = Ni_XY.data

		# print(Ni_X.size, Ni_Y.size, Ni_XY.size)

		if self.method == "grassberger":
			self.Hx = log(np.sum(Ni_X),self.log_type)-np.sum(Ni_X*spec.digamma(Ni_X))/np.sum(Ni_X)
			self.Hy = log(np.sum(Ni_Y),self.log_type)-np.sum(Ni_Y*spec.digamma(Ni_Y))/np.sum(Ni_Y)
			self.Hxy = log(np.sum(Ni_XY),self.log_type)-np.sum(Ni_XY*spec.digamma(Ni_XY))/np.sum(Ni_XY)
			self.mi = self.Hx+self.Hy-self.Hxy
		elif self.method == "standard":
			self.Hx = -1*np.sum(Ni_X/np.sum(Ni_X)*log(Ni_X/np.sum(Ni_X),self.log_type))
			self.Hy = -1*np.sum(Ni_Y/np.sum(Ni_Y)*log(Ni_Y/np.sum(Ni_Y),self.log_type))
			self.Hxy = -1*np.sum(Ni_XY/np.sum(Ni_XY)*log(Ni_XY/np.sum(Ni_XY),self.log_type))
			self.mi = self.Hx+self.Hy-self.Hxy

class MutualInformation(object):
	def __init__(self, corpusData, log_type, no_of_threads, data_file_path, overlap, method, cutoff):
		global corpus
		global dataArray
		global lineLengthList
		global totalLength
		corpus = corpusData
		dataArray = array.array('L', corpus.sequentialData.dataArray)
		lineLengthList = np.array(corpus.sequentialData.wordCountList, dtype=np.uint64)
		totalLength = corpus.sequentialData.totalLength
		self.no_of_threads = no_of_threads
		self.filename = data_file_path
		self.overlap = overlap
		self.method = method
		self.log_type = log_type
		self.cutoff = cutoff
		self.mutualInformation = self.calculate_MI()

	def calculate_MI(self):
		mi = np.zeros([0,1])
		Hx = np.zeros([0,1])
		Hy = np.zeros([0,1])
		Hxy = np.zeros([0,1])
		d = 1

		print("Average String Length: ", int(corpus.sequentialData.averageLength))
		print("Total String Length: ", int(corpus.sequentialData.totalLength))

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
		else:
			print("File does not exist to load previous data")

		end = False
		f = open(self.filename,"w")
		f.write("data: "+corpus.datainfo+"\n")
		for i in range(len(mi)):
			f.write("d:"+str(i+1)+":"+str(mi[i])+","+str(Hx[i])+","+str(Hy[i])+","+str(Hxy[i])+"\n")
		
		try:
			max_distance = totalLength
			while d<max_distance and d<=self.cutoff and end==False:
				mi = np.append(mi,np.zeros(self.no_of_threads))
				Hx = np.append(Hx,np.zeros(self.no_of_threads))
				Hy = np.append(Hy,np.zeros(self.no_of_threads))
				Hxy = np.append(Hxy,np.zeros(self.no_of_threads))

				thread = []
				for i in range(self.no_of_threads):
					thread.append(myThread(d+i, self.overlap, self.log_type, self.method))

				for i in range(self.no_of_threads):
					thread[i].start()

				for i in range(self.no_of_threads):
					thread[i].join()

				for i in range(self.no_of_threads):
					if thread[i].complete == 1:
						end = True
						for j in range(i,self.no_of_threads):
							if mi[len(mi)-1]==0:
								mi = np.delete(mi,len(mi)-1)
								Hx = np.delete(Hx,len(Hx)-1)
								Hy = np.delete(Hy,len(Hy)-1)
								Hxy = np.delete(Hxy,len(Hxy)-1)
						break

					if np.isnan(thread[i].mi):
						end = True
						for j in range(i,self.no_of_threads):
							if mi[len(mi)-1]==0:
								mi = np.delete(mi,len(mi)-1)
								Hx = np.delete(Hx,len(Hx)-1)
								Hy = np.delete(Hy,len(Hy)-1)
								Hxy = np.delete(Hxy,len(Hxy)-1)
						break

					mi[d+i-1] = thread[i].mi
					Hx[d+i-1] = thread[i].Hx
					Hy[d+i-1] = thread[i].Hy
					Hxy[d+i-1] = thread[i].Hxy

					print(thread[i].d, thread[i].mi, thread[i].Hx, thread[i].Hy, thread[i].Hx+thread[i].Hy, thread[i].Hxy)
					f.write("d:"+str(d+i)+":"+str(mi[d+i-1])+","+str(Hx[d+i-1])+","+str(Hy[d+i-1])+","+str(Hxy[d+i-1])+"\n")
				
				d += self.no_of_threads

		except KeyboardInterrupt:
			print("Processed upto: "+str(d-1))

		f.close()

		return mi, Hy, Hy, Hxy