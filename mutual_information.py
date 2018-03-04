#!/usr/bin/env python

# System libs
import numpy as np
import sys
import threading
import gc
import os

class myThread(threading.Thread):
	def __init__(self, d):
		self.d = d
		self.mi = 0
		super(myThread, self).__init__()

	def run(self):
		pair_counts = np.zeros([len(corpus.dictionary.counter),len(corpus.dictionary.counter)])
		for index in range(corpus.sequentialData.total):
			if index+self.d>=corpus.sequentialData.total:
				break
			pair_counts[corpus.sequentialData.wordArray[index],corpus.sequentialData.wordArray[index+self.d]]+=1

		# PMI (Pointwise Mutual Information) calculated between joint probability of two Random Variables and marginal probability of the same Random Variables
		joint_prob = pair_counts/corpus.sequentialData.total
		temp = joint_prob/pxpy
		del pair_counts
		gc.collect()
		
		# Removing 0's to avoid log(0)
		temp[temp==0] = 1		
		pmi = np.zeros([len(corpus.dictionary.counter),len(corpus.dictionary.counter)])
		pmi = np.log2(temp)

		# Mutual Information is Expected Value over all the Pointwise Mutual Information
		self.mi = (joint_prob*pmi).sum()
		del pmi
		gc.collect()

class MutualInformation(object):
	def __init__(self, corpusData, no_of_threads, data_file_path):
		global corpus
		corpus = corpusData
		self.no_of_threads = no_of_threads
		self.filename = data_file_path
		self.mutualInformation = self.calculate_MI()

	def calculate_MI(self):
		global pxpy
		px = np.zeros([0,1])
		mi = np.zeros([0,1])

		for counts in corpus.dictionary.counter:
			px = np.append(px, corpus.dictionary.counter[counts])
		px = px.reshape(1,len(px))/corpus.sequentialData.total
		pxpy = px*np.transpose(px)

		end = False
		new = False
		d = 1

		# Check if already processing is done or new process ?
		if(os.path.exists(self.filename)):
			f = open(self.filename,"r")
			lines = f.readlines()
			f.close()

			temp = lines[0].split()
			if temp[0] == "data:" and temp[1] == corpus.datainfo:				
				for line in lines:
					temp = line.split(":")
					if temp[0] == "d":
						mi = np.append(mi,np.zeros(1))
						mi[int(temp[1])-1] = float(temp[2])
						d = int(temp[1])+1

		try:
			max_distance = corpus.sequentialData.total
			while d<max_distance and end==False:
				mi = np.append(mi,np.zeros(self.no_of_threads))
				thread = []
				for i in range(self.no_of_threads):
					thread.append(myThread(d+i))

				for i in range(self.no_of_threads):
					thread[i].start()

				for i in range(self.no_of_threads):
					thread[i].join()

				for i in range(self.no_of_threads):
					mi[d+i-1] = thread[i].mi
					print(thread[i].d, thread[i].mi)

				d += self.no_of_threads
		except KeyboardInterrupt:
			for i in range(self.no_of_threads):
				if mi[len(mi)-1]==0:
					mi = np.delete(mi,len(mi)-1)
						
		f = open(self.filename,"w")
		f.write("data: "+corpus.datainfo+"\n")
		for i in range(len(mi)):
			f.write("d:"+str(i+1)+":"+str(mi[i])+"\n")
		f.close()

		return mi