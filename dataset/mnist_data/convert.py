import gzip
import pickle
import numpy as np

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

f.close()

print "Done 1"

n_steps = 28*28
seed = 92916

if 'seed' in globals():
    rng_permute = np.random.RandomState(seed)
    idx_permute = rng_permute.permutation(n_steps)
else:
    idx_permute = np.random.permutation(n_steps)

train_x = train_x[:,idx_permute]
valid_x = valid_x[:,idx_permute]
test_x = test_x[:,idx_permute]

f = open("mnist_data_per_1.dat", "w")

for image in train_x:
	for val in image:
		f.write(str(val)+" ")

for image in valid_x:
	for val in image:
		f.write(str(val)+" ")

for image in test_x:
	for val in image:
		f.write(str(val)+" ")

f.close()

print "Done 2"

n_steps = 28*28
seed = 43537

if 'seed' in globals():
    rng_permute = np.random.RandomState(seed)
    idx_permute = rng_permute.permutation(n_steps)
else:
    idx_permute = np.random.permutation(n_steps)

train_x = train_x[:,idx_permute]
valid_x = valid_x[:,idx_permute]
test_x = test_x[:,idx_permute]

f = open("mnist_data_per_2.dat", "w")

for image in train_x:
	for val in image:
		f.write(str(val)+" ")

for image in valid_x:
	for val in image:
		f.write(str(val)+" ")

for image in test_x:
	for val in image:
		f.write(str(val)+" ")

f.close()