import gzip
import pickle
import numpy as np
import matplotlib.pyplot as plt

f = gzip.open("mnist.pkl.gz","rb")
train, valid, test = pickle.load(f)

train_x, train_y = train
valid_x, valid_y = valid
test_x, test_y = test

train_flat = train_x.flatten()
valid_flat = valid_x.flatten()
test_flat = test_x.flatten()

data = np.concatenate([train_flat,valid_flat,test_flat])

data = data[0:10000]

acf = np.correlate(data,data,"full")
plt.semilogx(acf[0:10000])
plt.show()
