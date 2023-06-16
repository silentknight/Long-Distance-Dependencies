#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["1","2","4","5","6","9","14","15","17","18","20"]

# f = open("marginal_dependence_<unk>_"+filenames[7], "r")
f = open("word_pair_dependence_"+filenames[1], "r")
lines = f.readlines()
f.close()

print("word_pair_dependence_"+filenames[1])

start = 0
end = 0
index = 0

sn = np.zeros([0,1])
wn = np.zeros([0,1])
ind = np.zeros([0,1])
wp = np.zeros([0,1])
mp = np.zeros([0,1])
sp = np.zeros([0,1])
temp = lines[0].split()

for line in lines:
	temp = line.strip().split(",")
	sn = np.append(sn,np.zeros(1))
	sn[index] = int(temp[0])
	wn = np.append(wn,np.zeros(1))
	wn[index] = int(temp[1])
	ind = np.append(ind,np.zeros(1))
	ind[index] = int(temp[2])
	wp = np.append(wp,np.zeros(1))
	wp[index] = int(temp[3])
	mp = np.append(mp,np.zeros(1))
	mp[index] = int(temp[4])
	sp = np.append(sp,np.zeros(1))
	sp[index] = int(temp[5])
	index+=1

with plt.style.context(('seaborn')):
	fig = plt.figure()
	ax1 = plt.subplot(231)
	plt.semilogx(np.arange(1,len(sn)+1), sn, "r-", label="Strong Negative")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	ax1.set_xlim(1, len(sn))
	lgd1 = ax1.legend(loc='upper right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax2 = plt.subplot(232)
	plt.semilogx(np.arange(1,len(wn)+1), wn, 'm-', label="Weak Negative")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	ax2.set_xlim(1, len(wn))
	lgd2 = ax2.legend(loc='lower right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax3 = plt.subplot(233)
	plt.semilogx(np.arange(1,len(ind)+1), ind, 'c-', label="Independent")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	ax3.set_xlim(1, len(ind))
	lgd3 = ax3.legend(loc='upper right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax4 = plt.subplot(234, sharex=ax1)
	plt.semilogx(np.arange(1,len(sp)+1), sp, "k-", label="Strong Positive")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	ax4.set_xlim(1, len(sp))
	ax4.set_xlabel('Distance between words, d', fontsize=12)
	lgd4 = ax4.legend(loc='upper right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax5 = plt.subplot(235, sharex=ax2)
	plt.semilogx(np.arange(1,len(wp)+1), wp, 'b-', label="Weak Positive")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	ax5.set_xlim(1, len(wp))
	ax5.set_xlabel('Distance between words, d', fontsize=12)
	lgd5 = ax5.legend(loc='lower right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	ax6 = plt.subplot(236, sharex=ax3)
	plt.semilogx(np.arange(1,len(mp)+1), mp, 'g-', label="Moderate Positive")
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	ax6.set_xlim(1, len(mp))
	ax6.set_xlabel('Distance between words, d', fontsize=12)
	lgd6 = ax6.legend(loc='lower right', shadow=True, fancybox=True, ncol=3, numpoints=1, prop={'size': 12})

	fig.text(0.06, 0.5, 'Number of Word Pairs in Sequence', fontsize=12, ha='center', va='center', rotation='vertical')
	fig.set_figwidth(12)
	fig.set_figheight(5.5)
	print(fig.get_figwidth())
	print(fig.get_figheight())

	plt.savefig('pmi_plots_wiki19L')
	plt.show()
