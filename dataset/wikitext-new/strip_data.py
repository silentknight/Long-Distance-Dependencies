#!/usr/bin/env python
import re

filename = 'test_103'
f = open(filename,'r')
lines = f.readlines()
f.close()

useless = 0
uselessLen = 0
notEnglish = 0
notEnglishLen = 0
lotOfUNK = 0
lotOfUNKLen = 0
newData = ''
try:
	for line in lines:
		# print(line)
		if line == ' \n' or (line[0] == ' ' and line[1] == '=' and line[2] == ' '):
			useless += 1
			uselessLen += len(line)
		else:
			count = line.count('<unk>')
			ratio = float(count)/float(len(line))

			if count > 10:
				lotOfUNK += 1
				lotOfUNKLen += len(line)
			elif len(line) < 100:
				notEnglish += 1
				notEnglishLen += len(line)
			else:
				newData += line

	print(useless)
	print(uselessLen)
	print(notEnglish)
	print(notEnglishLen)
	print(lotOfUNK)
	print(lotOfUNKLen)
	print(len(newData))

	f = open(filename,'r')
	print(len(f.read()))
	f.close()

	f = open('cleaned_'+filename,'w')
	f.write(newData)
	f.close()
except KeyboardInterrupt:
	print("Done")
