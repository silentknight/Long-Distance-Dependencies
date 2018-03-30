import numpy as np
cimport numpy as np
from cpython cimport array
import array

cpdef getJointRV(dataArray, unsigned long[:] lineLengthList, int totalLength, int d, int overlap):
	cdef array.array X = array.array('L', [])
	cdef array.array Y = array.array('L', [])	
	cdef unsigned long index = 0
	cdef unsigned long steps = 0
	cdef unsigned long last = 0
	cdef unsigned long nLines = lineLengthList.shape[0]
	cdef unsigned long i = 0

	if overlap == 1:
		lineLengthList[0] = totalLength
		nLines = 1

	for i in range(nLines):
		steps = lineLengthList[i]/d
		last = steps*d
		array.extend(X,dataArray[index:index+last-d])
		array.extend(Y,dataArray[index+d:index+last])
		index+=lineLengthList[i]

	unique_X, counts_X = np.unique(X, return_counts=True)
	unique_Y, counts_Y = np.unique(Y, return_counts=True)

	cdef unsigned long[:] Xi = unique_X.astype(np.uint64)
	cdef unsigned long nXi = len(unique_X)
	cdef unsigned long[:] Yi = unique_Y.astype(np.uint64)
	cdef unsigned long nYi = len(unique_Y)
	cdef unsigned long nPosX = np.max(unique_X)+1
	cdef unsigned long nPosY = np.max(unique_Y)+1
	cdef unsigned long[:] Pos_X = np.zeros(nPosX, dtype=np.uint64)
	cdef unsigned long[:] Pos_Y = np.zeros(nPosY, dtype=np.uint64)

	for i in range(nXi):
		Pos_X[Xi[i]] = i

	for i in range(nYi):
		Pos_Y[Yi[i]] = i

	XY = np.zeros((unique_X.size,unique_Y.size), dtype=np.uint64)
	cdef unsigned long[:,:] temp_XY = XY
	cdef unsigned long n = len(X)

	for index in range(n):
		temp_XY[Pos_X[X[index]]][Pos_Y[Y[index]]]+=1

	return counts_X, counts_Y, XY