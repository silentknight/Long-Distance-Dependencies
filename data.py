import os

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
        self.train = self.tokenize(os.path.join(path, 'train.txt'))
        self.valid = self.tokenize(os.path.join(path, 'valid.txt'))
        self.test = self.tokenize(os.path.join(path, 'test.txt'))

    def tokenize(self, path):
        """Tokenizes a text file."""
        assert os.path.exists(path)
        # Add words to the dictionary
        with open(path, 'r') as f:
            tokens = 0
            for line in f:
                words = line.split() + ['<eos>']
                tokens += len(words)
                for word in words:
                    wordID = self.dictionary.add_word(word)
                    self.sequentialData.add_to_list(wordID)