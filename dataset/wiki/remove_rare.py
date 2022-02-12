import time

def main():
	f = open("text8","r")
	data = f.read()
	f.close()

	str_list = data.split() 
	unique_words = set(str_list) 

	for word in unique_words:
		freq_count=str_list.count(word)
		if freq_count < 10:
			data = data.replace(" "+word+" "," <unk> ")
			print(word)

	f = open("text8-wo-r","w")
	f.write(data)
	f.close()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Stopped")