import re
from operator import itemgetter    
 
frequency = {}
open_file = open('train', 'r')
file_to_string = open_file.read()
words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)
 
for word in words:
    count = frequency.get(word,0)
    frequency[word] = count + 1

f = open('zipf_counts.log','w')     
for key, value in reversed(sorted(frequency.items(), key = itemgetter(1))):
    f.write( '%s - %d\n' % (key, value))
f.close()