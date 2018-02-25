#!/usr/bin/env python

# System libs
from __future__ import print_function
import numpy as np
import time

class MutualInformation(object):
	def __init__(self, corpusData):
		self.mutualInformation = self.calculate_MI(corpusData)

	def calculate_MI(self, corpus):
		px = np.empty([0,1])
		for counts in corpus.dictionary.counter:
			px = np.append(px, corpus.dictionary.counter[counts])
		px = px/corpus.sequentialData.total

		end = True
		d = 1
		pair_counts = 0

		print(time.time())
		while d<corpus.sequentialData.total and end==True:
			for i in range(len(corpus.dictionary.counter)):
				for j in range(len(corpus.dictionary.counter)):
					for index in range(corpus.sequentialData.total):
						print(corpus.sequentialData.wordArray[index], i, corpus.sequentialData.wordArray[index+d], j)
						if corpus.sequentialData.wordArray[index] == i and corpus.sequentialData.wordArray[index+d] == j:
							pair_counts += 1
							print("Present: ", corpus.dictionary.idx2word[i], corpus.dictionary.idx2word[j], pair_counts)
			d += 1
			pair_counts = 0
			print(d, time.time())

		print("Done", time.time())