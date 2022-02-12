#!/usr/bin/env python
import re
import num2words

filename = 'train'
f = open(filename,'r')
lines = f.readlines()
f.close()
index = 0
try:
	f = open("ptb_"+filename,'w')
	for line in lines:
		line = line.strip()
		line = line.lower()
		line = re.sub('[^a-zA-Z0-9 \n \. \- \\ \/ \* \' \# \$ \&]', ' ', line)
		line = line.replace(" unk ", " <unk> ")		
		line = re.sub(r"(\d+ )", "N", line)
		line = " ".join(line.split())+"\n"
		f.write(line)
		print 'Line no processed: {}/{}'.format(index, len(lines))
		index += 1
	f.close()	
except KeyboardInterrupt:
	print("Done")
