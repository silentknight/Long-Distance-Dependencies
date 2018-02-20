#!/usr/bin/env python

# System libs
from __future__ import print_function
import time

class MutualInformation(object):
	def __init__(self, corpusData):
		self.mutualInformation = self.calculatePMI(corpusData)

	def calculatePMI(self, corpus):
		print(corpus.dictionary.word2idx)
		time.sleep(10)
		print(corpus.dictionary.counter)
