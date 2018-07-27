#!/usr/bin/env python

# System libs
import numpy as np
import scipy.special as spec
import sys
import threading
import os
import lddCalc
import array

class myThread(threading.Thread):
	def __init__(self, d, overlap):
		self.d = d
		self.mi = 0
		self.Hx = 0
		self.Hy = 0
		self.Hxy = 0
		self.complete = False
		self.overlap = overlap
		super(myThread, self).__init__()

	def run(self):
		Ni_X, Ni_Y, Ni_XY = lddCalc.getJointRV(dataArray, lineLengthList, totalLength, self.d, self.overlap)		
		try:
			if Ni_X == 0 and Ni_Y == 0 and Ni_XY == 0:
				self.complete = True
				exit()
		except ValueError:
			pass

		self.Hx = np.log(np.sum(Ni_X))-np.sum(Ni_X*spec.digamma(Ni_X))/np.sum(Ni_X)
		self.Hy = np.log(np.sum(Ni_Y))-np.sum(Ni_Y*spec.digamma(Ni_Y))/np.sum(Ni_Y)
		Ni_XY = Ni_XY.reshape(Ni_X.size*Ni_Y.size)
		Ni_XY = np.delete(Ni_XY,np.where(Ni_XY==0)[0])
		self.Hxy = np.log(np.sum(Ni_XY))-np.sum(Ni_XY*spec.digamma(Ni_XY))/np.sum(Ni_XY)
		self.mi = self.Hx+self.Hy-self.Hxy

class MutualInformation(object):
	def __init__(self, corpusData, method, compute, log_type, no_of_threads, data_file_path, overlap):
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
		self.mutualInformation = self.calculate_MI()

	def calculate_MI(self):
		mi = np.zeros([0,1])
		Hx = np.zeros([0,1])
		Hy = np.zeros([0,1])
		Hxy = np.zeros([0,1])
		d = 1

		print("Average String Length: ", int(corpus.sequentialData.averageLength))

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
		f = open(self.filename,"w")
		f.write("data: "+corpus.datainfo+"\n")
		
		try:
			max_distance = totalLength
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

		f.close()

		return mi, Hy, Hy, Hxy