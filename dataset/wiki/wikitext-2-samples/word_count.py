#!/usr/bin/env python

import numpy as np

def main():
	data_stream = ""
	filename = 'train_4'
	data_stream += open(filename,'r').read()

	filename = 'test_4'
	data_stream += open(filename,'r').read()

	filename = 'valid_4'
	data_stream += open(filename,'r').read()
	
	data = np.array(data_stream.split())
	# data = np.array(list(open(filename,'r').read()))
	[unique_words, unique_index, counts] = np.unique(data, return_index=True, return_counts=True)

	sort_ind = counts.argsort()
	sorted_counts = counts[sort_ind[::-1]]
	sorted_unique_words = unique_words[sort_ind[::-1]]
	sorted_unique_index = unique_index[sort_ind[::-1]]

	f = open(filename+'_unique_sorted.log','w')
	for i in range(len(unique_words)):
		f.write("%20s %10d\n" % (sorted_unique_words[i], sorted_counts[i]))
	f.close()

if __name__ == '__main__':
	main()
