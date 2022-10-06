import re
from operator import itemgetter

dir = "wikitext-103/"

frequency = {}
open_file = open(dir+'trainR', 'r')
file_to_string = open_file.read()
open_file = open(dir+'test', 'r')
file_to_string += open_file.read()
open_file = open(dir+'valid', 'r')
file_to_string += open_file.read()
#words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)
words = file_to_string.split()

for word in words:
    count = frequency.get(word,0)
    frequency[word] = count + 1

f = open(dir+'zipf_counts.log','w')
for key, value in reversed(sorted(frequency.items(), key = itemgetter(1))):
    f.write( '%s - %d\n' % (key, value))
f.close()
