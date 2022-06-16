#!/usr/bin/env python

import random
import numpy as np

f = open("SP2_V4_10000.dat","r")
data = f.readlines()
no_strings = len(data)
f.close()

print("Number of Lines", no_strings)
indexes = np.arange(0,no_strings)
random.shuffle(indexes)

new_data = ""
for index in indexes[0:5000]:
	new_data += data[index]

f = open("New_SP2_V4_10000.dat","w")
f.write(new_data)
f.close()
