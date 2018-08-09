#!/usr/bin/env python

# System libs
import numpy as np
import scipy.special as spec
import sys
import threading
import os
import lddCalc
import array
import json

class myThread(threading.Thread):
	def __init__(self, d, overlap, log_type, method):
		self.d = d
		self.Xi = 0
		self.Yi = 0
		self.Ni_X = 0
		self.Ni_Y = 0
		self.Ni_XY = 0
		self.pmi = 0
		self.complete = False
		self.overlap = overlap
		self.method = method
		self.log_type = log_type
		super(myThread, self).__init__()

	def run(self):
		Ni_X, Ni_Y, Ni_XY, self.Xi, self.Yi = lddCalc.getJointRV(dataArray, lineLengthList, totalLength, self.d, self.overlap)
		try:
			if Ni_X == 0 and Ni_Y == 0 and Ni_XY == 0:
				self.complete = True
				exit()
		except ValueError:
			pass

		log = lambda val,base: np.log(val) if base==0 else np.log2(val)

		if self.method == "standard":
			P_XY = Ni_XY/np.sum(Ni_XY)
			P_X = [Ni_X]/np.sum(Ni_X)
			P_Y = [Ni_Y]/np.sum(Ni_Y)
			denominator = (np.transpose(P_X)*P_Y)
			P_temp = P_XY/denominator
			P_temp[P_temp == 0] = 1
			self.pmi = P_XY*log(P_temp,self.log_type)
			self.Ni_X = Ni_X
			self.Ni_Y = Ni_Y
			self.Ni_XY = Ni_XY

class PointwiseMutualInformation(object):
	def __init__(self, corpusData, log_type, no_of_threads, data_file_path, overlap, method):
		global corpus
		global dataArray
		global lineLengthList
		global totalLength
		corpus = corpusData
		dataArray = array.array('L', corpus.sequentialData.dataArray)
		lineLengthList = np.array(corpus.sequentialData.wordCountList, dtype=np.uint64)
		totalLength = corpus.sequentialData.totalLength
		# self.no_of_threads = no_of_threads
		self.no_of_threads = 1
		self.directory = data_file_path
		self.overlap = overlap
		self.method = method
		self.log_type = log_type
		# Add more directories to create more refined data
		self.pointwiseMutualInformation = self.calculate_PMI()

	def calculate_PMI(self):
		d = 1
		print("Average String Length: ", int(corpus.sequentialData.averageLength))

		try:
			d_num = []
			files = sorted(os.listdir(self.directory))
			for file in files:
				d_num.append(int(file.split('.')[0]))

			d = sorted(d_num)[len(d_num)-1]+1
		except:
			print(self.directory+" does not exist")

		f = open(self.directory+"/0.symbols.dat","w")
		f.write(str(corpus.dictionary.word2idx))
		f.close()

		end = False
		try:
			max_distance = totalLength
			while d<max_distance and end==False:

				thread = []
				for i in range(self.no_of_threads):
					thread.append(myThread(d+i, self.overlap, self.log_type, self.method))

				for i in range(self.no_of_threads):
					thread[i].start()

				for i in range(self.no_of_threads):
					thread[i].join()
					# thread[i].pmi = thread[i].pmi.astype(np.float32)

					print(d)

					print(thread[i].Xi.dtype, thread[i].Yi.dtype, thread[i].Ni_X.dtype, thread[i].Ni_Y.dtype, thread[i].Ni_XY.dtype, thread[i].pmi.dtype)
					print(thread[i].Xi.nbytes, thread[i].Yi.nbytes, thread[i].Ni_X.nbytes, thread[i].Ni_Y.nbytes, thread[i].Ni_XY.nbytes, thread[i].pmi.nbytes)

					np.savez(self.directory+"/"+str(d), thread[i].Xi, thread[i].Yi, thread[i].Ni_X, thread[i].Ni_Y, thread[i].Ni_XY, thread[i].pmi)

				d += self.no_of_threads

		except KeyboardInterrupt:
			print("Processed upto: "+str(d+i))

		return 100
