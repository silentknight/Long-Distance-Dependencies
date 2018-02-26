#!/usr/bin/env python

# System libs
from __future__ import print_function
import numpy as np
import time

class MutualInformation(object):
	def __init__(self, corpusData):
		self.mutualInformation = self.calculate_MI(corpusData)

	def calculate_MI(self, corpus):
		pair_counts = np.zeros([len(corpus.dictionary.counter),len(corpus.dictionary.counter)])
		pmi = np.zeros([len(corpus.dictionary.counter),len(corpus.dictionary.counter)])
		px = np.zeros([0,1])
		mi = np.zeros([0,1])

		for counts in corpus.dictionary.counter:
			px = np.append(px, corpus.dictionary.counter[counts])
		px = px.reshape(1,len(px))/corpus.sequentialData.total
		pxpy = px*np.transpose(px)

		end = False
		d = 1
		while d<corpus.sequentialData.total and end==False:
			for index in range(corpus.sequentialData.total):
				if index+d>=corpus.sequentialData.total:
					break
				pair_counts[corpus.sequentialData.wordArray[index],corpus.sequentialData.wordArray[index+d]]+=1

			# PMI is Pointwose Mutual Information calcutaed between joint probability of two Random Variables and marginal probability of the same Random Variables
			joint_prob = pair_counts/corpus.sequentialData.total
			temp = joint_prob/pxpy
			# Removing 0's to avoid log(0)
			temp[temp==0] = 1
			pmi = np.log2(temp)

			# Mutual Information is Expected Value over all the Pointwise Mutual Information
			mi = (joint_prob*pmi).sum()
			print(d, mi)

			d += 1
			pair_counts = np.zeros([len(corpus.dictionary.counter),len(corpus.dictionary.counter)])