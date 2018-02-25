#!/usr/bin/env python

# System libs
from __future__ import print_function
import numpy as np

class MutualInformation(object):
	def __init__(self, corpusData):
		self.mutualInformation = self.calculate_MI(corpusData)

	def calculate_MI(self, corpus):
		px = np.empty([0,1])
		for counts in corpus.dictionary.counter:
			px = np.append(px, corpus.dictionary.counter[counts])
		px = px/corpus.sequentialData.total

		pmi = 