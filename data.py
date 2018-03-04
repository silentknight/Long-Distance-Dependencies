#!/usr/bin/env python

# System libs
import os
import sys
from collections import Counter

class Dictionary(object):
	def __init__(self):
		self.word2idx = {}
		self.idx2word = []
		self.counter = Counter()
		self.total = 0

	def add_word(self, word):
		if word not in self.word2idx:
			self.idx2word.append(word)
			self.word2idx[word] = len(self.idx2word) - 1

		token_id = self.word2idx[word]
		self.counter[token_id] += 1
		self.total += 1
		return self.word2idx[word]

	def get_word_from_id(self, wordID):
		return self.idx2word[wordID]

	def __len__(self):
		return len(self.idx2word)

class SequentialData(object):
	def __init__(self):
		self.wordArray = []
		self.total = 0

	def add_to_list(self, wordID):
		self.wordArray.append(wordID)
		self.total += 1

class Corpus(object):
	def __init__(self, path):
		self.dictionary = Dictionary()
		self.sequentialData = SequentialData()
		self.datainfo = path
		self.completion = self.choose_dataset(self.datainfo)

	def choose_dataset(self, path):
		if path=="dataset/dl4mt/":
			print("Penn Tree Bank from LSTM code")
			self.train = self.tokenize(os.path.join(path, 'train.txt'))
			self.valid = self.tokenize(os.path.join(path, 'valid.txt'))
			self.test = self.tokenize(os.path.join(path, 'test.txt'))
		elif path=="dataset/wiki/wikitext-2/":
			print("wikitext-2 dataset")
			self.train = self.tokenize(os.path.join(path, 'train'))
			self.valid = self.tokenize(os.path.join(path, 'valid'))
			self.test = self.tokenize(os.path.join(path, 'test'))
		elif path=="dataset/wiki/wikitext-103/":
			print("wikitext-103 dataset")
			self.train = self.tokenize(os.path.join(path, 'train'))
			self.valid = self.tokenize(os.path.join(path, 'valid'))
			self.test = self.tokenize(os.path.join(path, 'test'))
		else:
			print("Please check the dataset path supplied. No such path found")
			sys.exit(0)

		return 1

	def tokenize(self, path):
		"""Tokenizes a text file."""
		assert os.path.exists(path)
		# Add words to the dictionary
		with open(path, 'r') as f:
			tokens = 0
			for line in f:
				# words = line.split() + ['<eos>']
				words = list(line.strip().replace("<unk>", "^"))+[" "]
				tokens += len(words)
				for word in words:
					wordID = self.dictionary.add_word(word)
					self.sequentialData.add_to_list(wordID)