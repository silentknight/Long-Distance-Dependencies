#!/usr/bin/env python

import csv
import numpy as np
import simplejson

#############################
#Read allusers
file = open('trace.csv', 'rU')
f = csv.reader(file)
user_trace = []

for row in f:
  user_trace.append(row)

np_user_trace= np.array(user_trace)

#################################
user_grids = np_user_trace[:,3].tolist()

f = open('user_grids.txt', 'w')

simplejson.dump(user_grids, f)

f.close()