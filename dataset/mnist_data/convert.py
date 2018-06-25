import gzip
import pickle

f = gzip.open("mnist.pkl.gz","rb")
train, valid, test = pickle.load(f)

train_x, train_y = train
valid_x, valid_y = valid
test_x, test_y = test

f = open("mnist_data_un.dat", "w")

for image in train_x:
	for val in image:
		f.write(str(val)+" ")

for image in valid_x:
	for val in image:
		f.write(str(val)+" ")


for image in test_x:
	for val in image:
		f.write(str(val)+" ")
