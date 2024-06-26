#!/usr/bin/env python

import numpy as np

data_points = np.array([[1,75427,1265057,71670961219,4998715,4726094,3713],[4,6683,2596729,71659012922,11530096,8882294,1501],[35,483,2716901,71656335842,13502894,9473450,655],[3000,4,2789134,71654822022,14705961,9712928,175]])

print("Between 1 and db1")
for j in range(1,7):
		print("Dataset: w1={data_1:12d}, w2={data_2:12d}, gc={data_p:e}".format(data_1=data_points[0,j],data_2=data_points[1,j],data_p=(data_points[1,j]-data_points[0,j])/(data_points[1,0]-data_points[0,0])))

print("Between dr1 and db2")
for j in range(1,7):
		print("Dataset: w1={data_1:12d}, w2={data_2:12d}, gc={data_p:e}".format(data_1=data_points[2,j],data_2=data_points[3,j],data_p=(data_points[3,j]-data_points[2,j])/(data_points[3,0]-data_points[2,0])))