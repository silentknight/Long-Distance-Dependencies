#!/usr/bin/env python

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# filenames = ['wiki2', 'wiki_sample_1', 'wiki_sample_2', 'wiki_sample_3', 'wiki_sample_4']
# filenames = ['SP2_V4_20','SP4_V4_20','SP2_V26_20','SP4_V26_20']
# filenames = ['wiki103','wiki2']
filenames = ['text8','text8-small','text8-small-wo-r-2','text8-small-wo-r-4']
all_words = []
all_counts = []
max_len = 0

powerlaw = lambda x, amp, index: amp * (x**index)

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

	xdata = np.arange(1,len(counts)+1)
	ydata = np.array(counts)

	yerr = 1 * ydata[0:10000]

	logx = np.log(xdata[0:10000])
	logy = np.log(ydata[0:10000])
	logyerr = yerr / ydata[0:10000]

	fitfunc = lambda p, x: p[0] + p[1] * x
	errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

	pinit = [0, -1.0]
	out = optimize.leastsq(errfunc, pinit, args=(logx, logy, logyerr), full_output=1)

	pfinal = out[0]
	covar = out[1]
	index = pfinal[1]
	amp = 10.0**pfinal[0]

	indexErr = np.sqrt(covar[1][1])
	ampErr = np.sqrt(covar[0][0])*amp

	print(filename,index,indexErr,amp,ampErr)

	all_words.append(words)
	all_counts.append(counts)

with plt.style.context(('seaborn')):
	ax = plt.axes()

	plt.loglog(np.arange(1,len(all_counts[0])+1), all_counts[0], label="Text8: "+r'$\alpha$'+" = -1.0563")
	# plt.loglog(all_counts[0], powerlaw(np.array(all_counts[0]).astype(float), 1e6, -1.056310487080293), label="First Fit")

	plt.loglog(np.arange(1,len(all_counts[1])+1), all_counts[1], label="Text8 (Small): "+r'$\alpha$'+" = -1.0550")
	# plt.loglog(all_counts[1], powerlaw(np.array(all_counts[1]).astype(float), 0.2*1e6, -1.05507833693917), label="Second Fit")

	plt.loglog(np.arange(1,len(all_counts[2])+1), all_counts[2], label="Text8 (w/o Rare Small): "+r'$\alpha$'+" = -1.0573")
	# plt.loglog(all_counts[2], powerlaw(np.array(all_counts[2]).astype(float), 0.2*1e6, -1.0573763273014645), label="Third Fit")

	plt.loglog(np.arange(1,len(all_counts[3])+1), all_counts[3], label="Text8 (w/o Rare (4) Small): "+r'$\alpha$'+" = -1.0576")
	# plt.loglog(all_counts[3], powerlaw(np.array(all_counts[3]).astype(float), 0.2*1e6, -1.0576934993354605), label="Fourth Fit")

	plt.tick_params(labelsize='large', width=5)
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	ax.set_xlim(1, max_len+1)
	plt.xlabel('Characters', fontsize=15)
	plt.ylabel('Frequency', fontsize=15)
	lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=1, numpoints=1, prop={'size': 12})
	plt.savefig('zipf_plots_text', bbox_extra_artists=(lgd,), bbox_inches='tight')
	plt.show()