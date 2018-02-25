#!/usr/bin/env python

# System libs
from __future__ import print_function
import time

class MutualInformation(object):
	def __init__(self, corpusData):
		self.mutualInformation = self.calculateMI(corpusData)

	def calculateMI(self, corpus):
		print(corpus.sequentialData.wordArray)
		time.sleep(10)
		print(corpus.sequentialData.length)
