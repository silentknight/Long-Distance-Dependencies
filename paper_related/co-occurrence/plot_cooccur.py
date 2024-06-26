#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: '/mnt/data/pmi_data/penn_tree_words_standard_logx',
# 2: '/mnt/data/pmi_data/text8_words_standard_logx',
# 3: None,
# 4: '/mnt/data/pmi_data/text8_subset_standard_logx',
# 5: '/mnt/data/pmi_data/text8_subset_wor_standard_logx',
# 6: '/mnt/data/pmi_data/wiki2_words_standard_logx',
# 7: None,
# 8: None,
# 9: '/mnt/data/pmi_data/wiki103_words_standard_logx',
# 10: None,
# 11: None,
# 12: None,
# 13: None,
# 14: '/mnt/data/pmi_data/wiki_sample_3_words_standard_logx',
# 15: '/mnt/data/pmi_data/wiki_sample_4_words_standard_logx',
# 16: None,
# 17: '/mnt/data/pmi_data/wiki19_standard_logx',
# 18: '/mnt/data/pmi_data/wiki19L_standard_logx',
# 19: None,
# 20: '/mnt/data/pmi_data/text8_subset_wor_4_standard_logx'


filenames = ["1","2","4","5","6","9","12","13","14","15","17","18","20"]
# indexes = [ 0,  1,  2,  3,  4,  5,  6,   7,   8,   9,   10,  11,  12]

# f = open("marginal_dependence_<unk>_"+filenames[8], "r")
f = open("word_pair_dependence_"+filenames[5], "r")
lines = f.readlines()
f.close()

# print("marginal_dependence_<unk>"+filenames[8])
print("word_pair_dependence_"+filenames[5])

start = 0
end = 0
index = 0

# lines = lines[:-10000]

d = np.zeros([len(lines)])
sn = np.zeros([len(lines)])
wn = np.zeros([len(lines)])
ind = np.zeros([len(lines)])
wp = np.zeros([len(lines)])
mp = np.zeros([len(lines)])
sp = np.zeros([len(lines)])

for line in lines:
	temp = line.strip().split(",")
	d[index] = int(temp[0])
	sn[index] = int(temp[1])
	wn[index] = int(temp[2])
	ind[index] = int(temp[3])
	wp[index] = int(temp[4])
	mp[index] = int(temp[5])
	sp[index] = int(temp[6])
	index+=1

total = sn+wn+wp+mp+sp

with plt.style.context(('seaborn')):
	fig = plt.figure()

	ax1 = plt.subplot(231)
	plt.semilogx(d, total, 'c-', label="All Unique Word Pairs")
	# plt.plot(d, total, 'c-', label="All Unique Word Pairs")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	# ax1.set_xlim(1, len(ind))
	lgd3 = ax1.legend(loc='lower right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax2 = plt.subplot(232)
	plt.semilogx(d, sn, "r-", label="Strong Negative \nDependent Word Pairs")
	# plt.plot(d, sn, "r-", label="Strong Negative")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	# ax2.set_xlim(1, len(sn))
	lgd1 = ax2.legend(loc='upper right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax3 = plt.subplot(233)
	plt.semilogx(d, wn, 'm-', label="Weak Negative \nDependent Word Pairs")
	# plt.plot(d, wn, 'm-', label="Weak Negative")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	# ax3.set_xlim(1, len(wn))
	lgd2 = ax3.legend(loc='lower right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax4 = plt.subplot(234, sharex=ax1)
	plt.semilogx(d, sp, "k-", label="Strong Positive \nDependent Word Pairs")
	# plt.plot(d, sp, "k-", label="Strong Positive")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	# ax4.set_xlim(1, len(sp))
	ax4.set_xlabel('Word Pair Lag, d', fontsize=12)
	lgd4 = ax4.legend(loc='upper right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax5 = plt.subplot(235, sharex=ax2)
	plt.semilogx(d, mp, 'g-', label="Moderate Positive \nDependent Word Pairs")
	# plt.plot(d, mp, 'g-', label="Moderate Positive")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	# ax5.set_xlim(1, len(mp))
	ax5.set_xlabel('Word Pair Lag, d', fontsize=12)
	lgd6 = ax5.legend(loc='lower right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax6 = plt.subplot(236, sharex=ax3)
	plt.semilogx(d, wp, 'b-', label="Weak Positive \nDependent Word Pairs")
	# plt.plot(d, wp, 'b-', label="Weak Positive")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	# ax6.set_xlim(1, len(wp))
	ax6.set_xlabel('Word Pair Lag, d', fontsize=12)
	lgd5 = ax6.legend(loc='lower right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	fig.text(0.06, 0.5, 'Number of Word Pairs in Natural Language', fontsize=12, ha='center', va='center', rotation='vertical')
	fig.set_figwidth(12)
	fig.set_figheight(5.5)
	print(fig.get_figwidth())
	print(fig.get_figheight())

	plt.savefig('pmi_plots_wiki103')
	plt.show()
