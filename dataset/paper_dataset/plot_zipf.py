#!/usr/bin/env python

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

filenames = ['wiki2', 'wiki_sample_1', 'wiki_sample_2', 'wiki_sample_3', 'wiki_sample_4']

all_words = []
all_counts = []
max_len = 0

for filename in filenames:
	words = []
	counts = []

	f = open(filename+'_unique_sorted.log','r')
	lines = f.readlines()
	f.close()

	for line in lines:
		[word, count] = line.split()
		words.append(word)
		counts.append(int(count))

	if len(counts)>max_len:
		max_len = len(counts)

	all_words.append(words)
	all_counts.append(counts)

with plt.style.context(('seaborn')):
	ax = plt.axes()

	plt.loglog(np.arange(1,len(all_counts[1])+1), all_counts[1], label="WikiText Sample 1")
	plt.loglog(np.arange(1,len(all_counts[2])+1), all_counts[2], label="WikiText Sample 2")
	plt.loglog(np.arange(1,len(all_counts[3])+1), all_counts[3], label="WikiText Sample 3")
	plt.loglog(np.arange(1,len(all_counts[4])+1), all_counts[4], label="WikiText Sample 4")
	plt.loglog(np.arange(1,len(all_counts[0])+1), all_counts[0], label="WikiText2")

	plt.tick_params(labelsize='large', width=5)
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	ax.set_xlim(1, max_len+1)
	plt.xlabel('Characters', fontsize=15)
	plt.ylabel('Frequency', fontsize=15)
	lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=2, numpoints=1, prop={'size': 12})
	plt.savefig('zipf_plots', bbox_extra_artists=(lgd,), bbox_inches='tight')
	plt.show()