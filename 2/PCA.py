#!/usr/bin/env python3
import numpy as np
import random

def loadpgm(path):
	f = open(path, 'rb')
	f.read(0xd)
	return list(f.read(92 * 112))

	
def PCA(traindata, testdata, threshold):
	sigma = 0
	z = 0
	for i in traindata:
		sigma += np.array([i]).T * np.array([i])
		z += 1
		print(z)
	u, s, vh = np.linalg.svd(sigma)
	return u

def predict(traindata, testdata):
	bingo = 0
	for i in range(40):
		for j in range(2):
			z = [np.sum(np.abs(x - testdata[i * 2 + j])) for x in traindata]
			m = z[0]
			midx = 0
			for k in range(40 * 8):
				if z[k] < m:
					m = z[k]
					midx = k
			if midx//8 == i:
				bingo += 1
	print(bingo/80)


# load data
traindata = []
testdata = []
for i in range(40):#40 persons
	x = list(range(10))
	random.shuffle(x)
	for j in range(8):
		traindata.append(loadpgm('faces/s%d/%d.pgm'%(i+1, x[j] + 1)))
	for j in range(2):
		testdata.append(loadpgm('faces/s%d/%d.pgm'%(i+1, x[j+8] + 1)))

print(traindata.__str__().replace())

traindata = np.array(traindata)
testdata = np.array(testdata)

# feature scaling
mean_traindata = np.mean(traindata, 0)
for i in range(len(traindata)):
	traindata[i] = traindata[i] - mean_traindata
for i in range(len(testdata)):
	testdata[i] = testdata[i] - mean_traindata


# PCA
#u = PCA(traindata, testdata, 1)
#print(u)




# predict

		
