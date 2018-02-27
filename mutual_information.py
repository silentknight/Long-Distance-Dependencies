#!/usr/bin/env python

# System libs
from __future__ import print_function
import numpy as np
import sys
import threading
import gc
import time

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

		# PMI is Pointwose Mutual Information calcutaed between joint probability of two Random Variables and marginal probability of the same Random Variables
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
	def __init__(self, corpusData):
		global corpus
		corpus = corpusData
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
		d = 1
		batch_size = 4

		try:
			startTime=time.time()
			print("Start Time: ", startTime)

			while d<corpus.sequentialData.total and end==False:
				mi = np.append(mi,np.zeros(batch_size))
				thread = []
				for i in range(batch_size):
					thread.append(myThread(d+i))

				for i in range(batch_size):
					thread[i].start()

				for i in range(batch_size):
					thread[i].join()

				for i in range(batch_size):
					mi[d+i-1] = thread[i].mi
					print(thread[i].d, thread[i].mi)

				d += batch_size

				print(time.time()-startTime)
				startTime = time.time()
		except KeyboardInterrupt:
			return mi