#!/usr/bin/env python3
import numpy as np
import random

def loadpgm(path):
	f = open(path, 'rb')
	f.read(0xd)
	return list(f.read(92 * 112))

	
def PCA(traindata, testdata, threshold):
	sigma = 0
	sigma = traindata.T * traindata
	sigma = sigma / 320
	
	w, v = np.linalg.eig(sigma)
	w = w.real
	v = v.real
	se = sum(w) * threshold
	ze = 0
	i = 0
	while True:
		ze += w[i]
		i += 1
		if ze >= se or i > len(w):
			break
	return v[:i]


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


traindata = np.mat(traindata)
testdata = np.mat(testdata)

# feature scaling
mean_traindata = np.mean(traindata, 0)
for i in range(len(traindata)):
	traindata[i] = traindata[i] - mean_traindata
for i in range(len(testdata)):
	testdata[i] = testdata[i] - mean_traindata


# PCA
u = PCA(traindata, testdata, 0.9)

# predict
traindata = traindata * u.T
testdata = testdata * u.T
predict(traindata, testdata)
		
