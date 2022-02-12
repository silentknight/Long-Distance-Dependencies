dir = 'wikitext-19/'

f = open(dir+"train", "r")
data = f.read()
words = data.split() + ['<eos>']
words = set(words)
f.close()
train_words = []
for word in words:
	train_words.append(word.strip())
print(len(train_words))

f = open(dir+"test", "r")
data = f.read()
test_lines = data.splitlines()
words = data.split() + ['<eos>']
words = set(words)
f.close()
test_words = []
for word in words:
	test_words.append(word.strip())
print(len(test_words))

f = open(dir+"valid", "r")
data = f.read()
valid_lines = data.splitlines()
words = data.split() + ['<eos>']
words = set(words)
f.close()
valid_words = []
for word in words:
	valid_words.append(word.strip())
print(len(valid_words))

outfile = ""
unused_test_words = []
unused_valid_words = []
for test_word in test_words:
	if test_word in train_words:
		None
	else:
		unused_test_words.append(test_word)
for valid_word in valid_words:
	if valid_word in train_words:
		None
	else:
		unused_valid_words.append(valid_word)

print(len(unused_test_words))
print(len(unused_valid_words))

raw_input("Press to continue")

outfile = ""
for line in test_lines:
	for word in unused_test_words:
		line = line.replace(' '+word+' ', ' <unk> ')
	outfile += line + "\n"
with open(dir+'test_new', 'w') as file:
	file.write(outfile)

outfile = ""
for line in valid_lines:
	for word in unused_valid_words:
		line = line.replace(' '+word+' ', ' <unk> ')
	outfile += line + "\n"
with open(dir+'valid_new', 'w') as file:
	file.write(outfile)

