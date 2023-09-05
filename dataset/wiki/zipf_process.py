import re
from operator import itemgetter
import time

dir = "wikitext-2/"

frequency = {}
open_file = open(dir+'train', 'r')
file_to_string = open_file.read()
open_file = open(dir+'test', 'r')
file_to_string += open_file.read()
open_file = open(dir+'valid', 'r')
file_to_string += open_file.read()
# words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)
words = file_to_string.split()

for i in range(2000000,len(words)):
    sub_words = ' '.join(words[0:i]).split()

    for word in sub_words:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        if frequency[word] == 1:
            print('%d/%d : %s' % (i, len(words), word))