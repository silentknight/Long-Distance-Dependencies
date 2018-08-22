import numpy as np
cimport numpy as np
from cpython cimport array
import array
import scipy.sparse


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
		if steps > 1:
			array.extend(X,dataArray[index:index+last-d])
			array.extend(Y,dataArray[index+d:index+last])
			index+=lineLengthList[i]

	if len(X) == 0 or len(Y) == 0:
		return 0,0,0

	unique_X, counts_X = np.unique(X, return_counts=True)
	unique_Y, counts_Y = np.unique(Y, return_counts=True)

	nuXi = len(unique_X)
	nuYi = len(unique_Y)

	temp_sp = scipy.sparse.coo_matrix((np.ones(len(X)), (np.asarray(X), np.asarray(Y))), shape=(max(X)+1, max(Y)+1))
	XY = temp_sp.tocsc()

	return counts_X, counts_Y, XY, unique_X, unique_Y


cpdef getStandardPMI(P_XY_data, P_XY_row, P_XY_col, PX, PY, unsigned long dataLen, unsigned long pxLen, unsigned long pyLen, int base):

	cdef extern from "math.h":
		cdef double log(double x)
		cdef double log2(double x)

	cdef double[:] data = P_XY_data
	cdef unsigned long[:] row = P_XY_row
	cdef unsigned long[:] col = P_XY_col
	cdef double[:] px = PX
	cdef double[:] py = PY
	cdef unsigned long i = 0
	cdef double denominator;

	pmi = np.zeros(dataLen, dtype=np.float64)
	cdef double[:] temp_pmi = pmi

	for i in range(dataLen):
		denominator = px[row[i]]*py[col[i]]

		if base == 0:
			temp_pmi[i] = log(data[i]/denominator)
		elif base == 1:
			temp_pmi[i] = log2(data[i]/denominator)

	return pmi