#!/usr/bin/env python
import csv
import numpy as np
import simplejson


#Clean CSV
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

#user_grids1 = []

#for i in range(len(user_grids)):

# if(i%8 == 0):

#    user_grids1.append(user_grids[i])

f = open('user_grids.txt', 'w')

simplejson.dump(user_grids, f)

f.close()


'''
file = open('/Users/admin/Desktop/SigSpatial2018/code/Long-Distance-Dependencies/dataset/mobility/user_poi.csv', 'rU')
f = csv.reader(file)
user_trace = []

for row in f:
  user_trace.append(row)

user_poi = []

for i in range(len(user_trace[0])):
  if(i%2 == 0):
    user_poi.append(user_trace[0][i])

my_file = open('user_pois.txt', 'w')

for item in user_poi:
  my_file.write("%s\n" % item)

my_file.close()
'''
