import time

def main():
	f = open("train","r")
	data = f.read()
	f.close()

	str_list = data.split()
	unique_words = set(str_list)
	print(len(unique_words))

	rejected = 0
	for word in unique_words:
		freq_count = str_list.count(word)
		if freq_count < 2:
			print(rejected,word,freq_count)
			data = data.replace(" "+word+" "," <unk> ")
			rejected += 1
			if rejected > (len(unique_words)-33100):
				break

	f = open("train_new","w")
	f.write(data)
	f.close()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Stopped")
