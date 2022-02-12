#!/usr/bin/env python
import re
import num2words

filename = 'train'
f = open(filename,'r')
lines = f.readlines()
f.close()
index = 0
try:
	f = open("text8"+filename,'a')
	for line in lines:
		line = line.lower()
		line = re.sub('[^a-zA-Z0-9 \n]', ' ', line)
		line = line.replace(" unk ", " <unk> ")
		line = re.sub('(\d+(\.\d+)?)', r' \1 ', line)
		line = re.sub(r"(\d+)", lambda x: ' '.join([d for d in x.group(0)]), line)
		line = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), line)
		line = " ".join(line.split())+"\n"
		f.write(line)
		print 'Line no processed: {}/{}'.format(index, len(lines))
		index += 1
	f.close()	
except KeyboardInterrupt:
	print("Done")
