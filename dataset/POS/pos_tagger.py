from flair.data import Sentence
from flair.models import SequenceTagger
import sys

filename = "dl4mt/train"

universal_tags = ["<ADJ>","<ADP>","<ADV>","<AUX>","<CCONJ>","<DET>","<INTJ>","<NOUN>","<NUM>","<PART>","<PRON>","<PROPN>","<PUNCT>","<SCONJ>","<SYM>","<VERB>","<X>"]

f = open(filename,"r")
lines = f.readlines()
f.close()
print(filename)

tagger = SequenceTagger.load('pos-multi')

totalLines = len(lines)
index = 0
f = open(filename+"-pos","w")
for line in lines:
	sentence = Sentence(line)
	tagger.predict(sentence)
	tagged_line = sentence.to_tagged_string()
	tags = tagged_line.split()

	write_data = ""
	for tag in tags:
		if (tag in universal_tags):
			write_data += tag+" "
	f.write(write_data)
	index +=1
	sys.stdout.write("\rCompleted: %5.2f%%" % (index/totalLines*100))
	sys.stdout.flush()
f.close()