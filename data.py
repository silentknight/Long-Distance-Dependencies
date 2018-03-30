#!/usr/bin/env python

# System libs
import os
import sys
from collections import Counter
import simplejson as json

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
		self.__wordLine = []
		self.wordArray = []
		self.dataArray = []
		self.wordCountList = []
		self.averageLength = 0
		self.totalLength = 0

	def add_to_list(self, wordID):
		self.__wordLine.append(wordID)

	def add_data(self, concatenate):
		if concatenate:
			self.wordArray = self.wordArray+self.__wordLine
			self.dataArray = self.dataArray+self.__wordLine
		else:
			self.wordArray.append(self.__wordLine)
			self.dataArray = self.dataArray+self.__wordLine

		self.averageLength = (self.averageLength*len(self.wordCountList)+len(self.__wordLine))/(len(self.wordCountList)+1)
		self.wordCountList.append(len(self.__wordLine))
		self.totalLength += len(self.__wordLine)
		self.__wordLine = []

class Corpus(object):
	def __init__(self, path, concatenate):
		self.dictionary = Dictionary()
		self.sequentialData = SequentialData()
		self.datainfo = path
		self.concatenate = concatenate
		self.completion = self.choose_dataset(self.datainfo)

	def choose_dataset(self, path):
		if path=="dataset/dl4mt/":
			print("Penn Tree Bank from LSTM code")
			self.train = self.tokenize_file(os.path.join(path, 'train.txt'), self.concatenate) 
			self.valid = self.tokenize_file(os.path.join(path, 'valid.txt'), self.concatenate)
			self.test = self.tokenize_file(os.path.join(path, 'test.txt'), self.concatenate)
		elif path=="dataset/wiki/wikitext-2/":
			print("wikitext-2 dataset")
			self.train = self.tokenize_file(os.path.join(path, 'train'), self.concatenate)
			self.valid = self.tokenize_file(os.path.join(path, 'valid'), self.concatenate)
			self.test = self.tokenize_file(os.path.join(path, 'test'), self.concatenate)
		elif path=="dataset/wiki/wikitext-103/":
			print("wikitext-103 dataset")
			self.train = self.tokenize_file(os.path.join(path, 'train'), self.concatenate)
			self.valid = self.tokenize_file(os.path.join(path, 'valid'), self.concatenate)
			self.test = self.tokenize_file(os.path.join(path, 'test'), self.concatenate)
		elif path=="dataset/foma/":
			print("foma dataset")
			dataset = os.path.join(path, 'Original_Data/SP/SP8')
			self.process_foma(dataset)
		elif path=="dataset/music/":
			dataset = os.path.join(path, 'tunes.json')
			self.process_music(dataset)
		else:
			print("Please check the dataset path supplied. No such path found")
			sys.exit(0)
		return 1

	def tokenize_file(self, path, concatenate):
		assert os.path.exists(path)
		with open(path, 'r') as f:
			tokens = 0
			for line in f:
				# words = line.split() + ['<eos>']
				words = list(line.strip().replace("<unk>", "^"))+[" "]
				tokens += len(words)
				for word in words:
					wordID = self.dictionary.add_word(word)
					self.sequentialData.add_to_list(wordID)
		self.sequentialData.add_data(concatenate)

	def tokenize_strings(self, line, concatenate):
		tokens = 0
		words = list(line)
		tokens += len(words)
		for word in words:
			wordID = self.dictionary.add_word(word)
			self.sequentialData.add_to_list(wordID)
		self.sequentialData.add_data(concatenate)

	def process_foma(self, path):
		try:
			for root,dirs,files in os.walk(path):
				files.sort()
				for name in files:
					filename = os.path.join(root,name)
					print("File being processed: ", filename)
					f = open(filename, "r")
					lines = f.readlines()
					f.close()
					for line in lines:
						temp = line.strip().split()
						if temp[1] == "TRUE":
							self.tokenize_strings(temp[0], self.concatenate)
		except TypeError:
			pass

	def process_music(self, path):
		f = open(path,"r")
		data = f.read()
		f.close()
		music_data = json.loads(data)
		for song in music_data:
			self.tokenize_strings(music_data[song], self.concatenate)