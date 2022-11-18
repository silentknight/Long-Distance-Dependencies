#!/usr/bin/env python

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot Zipf distribution')
parser.add_argument('--filename', type=str, required=True,
					help='Filename to analyze')
parser.add_argument('--index', type=int,
					help='Index of <UNK> token')
parser.add_argument('--end', type=int,
					help='Length of string')
args = parser.parse_args()

def main():
	words = []
	counts = []

	temp = args.filename.split('.')[0].split('_')
	last =len(temp)-2
	plot_filename = ""
	for i in range(last-1):
		plot_filename += temp[i]+'_'
	plot_filename += temp[last-1]

	f = open(args.filename,'r')
	lines = f.readlines()
	f.close()

	for line in lines:
		[word, count] = line.split()
		words.append(word)
		counts.append(int(count))

	print("Max x-axis:", len(counts))
	print("Max y-axis:", max(counts))

	area = sum(counts)

	threshold = 100

	head = sum(counts[0:threshold])
	tail = sum(counts[threshold:])

	print(area, head, head/area*100, tail, tail/area*100)

	# with plt.style.context(('seaborn')):
	# 	# ax = plt.axes()

	# 	if args.end:
	# 		end = args.end
	# 	else:
	# 		end = len(counts)

	# 	# plt.bar(words[0:end], counts[0:end], 0.4)
	# 	plt.loglog(counts)

	# 	plt.tick_params(labelsize='large', width=5)
	# 	plt.xlabel('Characters', fontsize=15)
	# 	plt.ylabel('Frequency', fontsize=15)
	# 	# current_values = plt.gca().get_yticks()
	# 	# plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])
	# 	# if args.index:
	# 	# 	plt.xticks(rotation=90)
	# 	# 	ax.set_xticks([args.index])

	# 	plt.savefig('zipf_'+plot_filename, bbox_inches='tight')
	# 	plt.show()

if __name__ == '__main__':
	main()