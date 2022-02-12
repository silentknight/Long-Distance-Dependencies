def freq(str): 

	str_list = str.split() 
	unique_words = set(str_list) 
	
	for words in unique_words:
		if str_list.count(words) <= 1:
			print(words+'-') 

if __name__ == "__main__": 

	f = open('trainwR')
	str = f.read()
	f.close()
	freq(str) 
