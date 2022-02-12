#!/usr/bin/env python

# System libs
import os
import sys
from collections import Counter
import simplejson as json
import gzip
import pickle


# Save this function in a file
class Dictionary(object):
	def __init__(self):
		self.word2idx = {}
		self.idx2word = []
		self.counter = Counter()
		self.total = 0

	# Cythoniza this function
	def add_word(self, word, inTrain):
		word = str(word)
		if word not in self.word2idx:
			if inTrain == 1:
				self.idx2word.append(word)
				self.word2idx[word] = len(self.idx2word) - 1
				token_id = self.word2idx[word]
				self.counter[token_id] += 1
				self.total += 1
			else:
				return -2
		return self.word2idx[word]

	def get_word_from_id(self, wordID):
		return self.idx2word[wordID]

	def __len__(self):
		return len(self.idx2word)


# Save this function in a file
class SequentialData(object):
	def __init__(self):
		self.__wordLine = []
		self.dataArray = []
		self.wordCountList = []
		self.averageLength = 0
		self.totalLength = 0

	# Cythoniza this function
	def add_to_list(self, wordID):
		self.__wordLine.append(wordID)

	# Cythoniza this function
	def add_data(self):
		self.dataArray = self.dataArray + self.__wordLine
		self.averageLength = (self.averageLength * len(self.wordCountList) + len(self.__wordLine)) / (len(self.wordCountList) + 1)
		self.wordCountList.append(len(self.__wordLine))
		self.totalLength += len(self.__wordLine)
		self.__wordLine = []


class Corpus(object):
	def __init__(self, ifwords):
		self.dictionary = Dictionary()
		self.sequentialData = SequentialData()
		self.ifwords = ifwords
		self.file = open("unused_words.txt","w")
		self.completion = self.choose_dataset()

	def choose_dataset(self):
		path = "."
		print("wikitext-X dataset")
		self.train = self.tokenize_file(os.path.join(path, 'train'), 1)
		self.valid = self.tokenize_file(os.path.join(path, 'valid'), 0)
		self.test = self.tokenize_file(os.path.join(path, 'test'), 0)

	def tokenize_file(self, path, inTrain):
		assert os.path.exists(path)
		print(path)
		with open(path, 'r') as f:
			tokens = 0
			for line in f:
				if self.ifwords == 1:
					words = line.split() + ['<eos>']
				else:
					words = list(line.strip().replace("<unk>", "^")) + [" "]

				tokens += len(words)
				for word in words:
					wordID = self.dictionary.add_word(word, inTrain)
					if wordID != -2:
						self.sequentialData.add_to_list(wordID)
					else:
						pass
						self.file.write(word+"\n")
		self.sequentialData.add_data()
		print("Size of Vocabulary", len(self.dictionary.counter))

data = Corpus(1)
print(data.sequentialData.totalLength)

f = open("unused_words.txt", "r")
words = set(f.readlines())
f.close()

print(len(words))

index = 0
for word in words:
	index += 1
	print(str(index)+" : "+word.strip())

	outfile1 = ""
	outfile2 = ""

	with open('test', 'r') as file :
		filedata1 = file.readlines()
	for line1 in filedata1:
		outfile1 += line1.replace(' '+word.strip()+' ', ' <unk> ')
	with open('test', 'w') as file:
		file.write(outfile1)

	with open('valid', 'r') as file :
		filedata2 = file.readlines()
	for line2 in filedata2:
		outfile2 += line2.replace(' '+word.strip()+' ', ' <unk> ')
	with open('valid', 'w') as file:
		file.write(outfile2)
