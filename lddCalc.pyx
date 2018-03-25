import numpy as np

def getJointRV(wordArray, d, overlap):
	if overlap == 1:
		X = [item for sublist in wordArray for item in sublist]
		X_new = np.array(X)
		steps = int(X_new.size/d)
		last = steps*d
		Y_new = X_new[d:last]
		X_new = X_new[0:last-d]
	elif overlap == 0:
		X = []
		Y = []
		for line in wordArray:
			steps = int(len(line)/d)
			last = steps*d
			X = X+line[0:last-d]
			Y = Y+line[d:last]
		X_new = np.array(X)
		Y_new = np.array(Y)

	unique_X, counts_X = np.unique(X_new, return_counts=True)
	unique_Y, counts_Y = np.unique(Y_new, return_counts=True)

	XY = np.zeros((unique_X.size,unique_Y.size))
	for index in range(X_new.size):
		XY[np.where(unique_X==X_new[index])[0][0],np.where(unique_Y==Y_new[index])[0][0]]+=1

	return counts_X, counts_Y, XY