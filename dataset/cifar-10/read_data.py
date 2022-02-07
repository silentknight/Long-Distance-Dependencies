import numpy as np
import matplotlib.pyplot as plt
import pickle

ifwords = 1

def tokenize_strings(line):
	tokens = 0
	if ifwords == 1:
		words = line.strip().split()
	else:
		words = list(line.strip())
	tokens += len(words)

	print(set(words), len(set(words)))
	# for word in words:
	# 	wordID = self.dictionary.add_word(word)
	# 	self.sequentialData.add_to_list(wordID)
	# self.sequentialData.add_data()
	# print("Size of Vocabulary", len(self.dictionary.counter))

def unpickle(file):
	with open(file, 'rb') as fo:
		data = pickle.load(fo, encoding='bytes')
	return data

def load_cifar_10_data(data_dir):
	meta_data_dict = unpickle(data_dir + "batches.meta")
	cifar_label_names = meta_data_dict[b'label_names']
	cifar_label_names = np.array(cifar_label_names)

	cifar_train_data = None
	cifar_train_filenames = []
	cifar_train_labels = []

	for i in range(1, 6):
		cifar_train_data_dict = unpickle(data_dir + "data_batch_{}".format(i))
		if i == 1:
			cifar_train_data = cifar_train_data_dict[b'data']
		else:
			cifar_train_data = np.vstack((cifar_train_data, cifar_train_data_dict[b'data']))
		cifar_train_filenames += cifar_train_data_dict[b'filenames']
		cifar_train_labels += cifar_train_data_dict[b'labels']

	cifar_test_data_dict = unpickle(data_dir + "test_batch")
	cifar_test_data = cifar_test_data_dict[b'data']
	cifar_test_filenames = cifar_test_data_dict[b'filenames']
	cifar_test_labels = cifar_test_data_dict[b'labels']

	return cifar_train_data, cifar_test_data

def process_cifar_10(path):
	data_dir = path
	channel = "red"
	train_data, test_data = load_cifar_10_data(data_dir)
	data = np.concatenate((train_data, test_data), axis=0)

	all_pixels = ""
	for i in range(data.shape[0]):
		[data_red, data_green, data_blue] = np.split(data[i],3)
		data_grayscale = 0.299*data_red + 0.587*data_green + 0.114*data_blue

		if channel == "red":
			pixel_values = data_red
		elif channel == "green":
			pixel_values = data_green
		elif channel == "red":
			pixel_values = data_blue
		elif channel == "gray":
			pixel_values = data_grayscale

		string_pixels = [str(pix) for pix in pixel_values]
		pixel_line = " ".join(string_pixels)
		pixel_line = pixel_line.strip()+" "
		all_pixels += pixel_line

	tokenize_strings(all_pixels)

if __name__ == "__main__":
	process_cifar_10("")