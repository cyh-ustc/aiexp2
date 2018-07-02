#!/usr/bin/env python3
import numpy as np
import random

# load images
def loadpgm(path):
	f = open(path, 'rb')
	f.read(0xd)
	return list(f.read(92 * 112))


def PCA(traindata, testdata, threshold):
	# compute sigma
	sigma = 0
	sigma = traindata.T * traindata
	sigma = sigma / 320
	# compute eigs
	w, v = np.linalg.eig(sigma)
	# ignore imag part
	w = w.real
	v = v.real
	# sum of eigs
	se = sum(w) * threshold
	ze = 0
	i = 0
	# select first i eigs sum(v[:i]) >= sum(v) * threshold
	while True:
		ze += w[i]
		i += 1
		if ze >= se or i > len(w):
			break
	return v[:i]

# predict
def predict(traindata, testdata):
	bingo = 0
	for i in range(40):
		for j in range(2):
			z = [np.sum(np.abs(x - testdata[i * 2 + j])) for x in traindata]
			m = z[0]
			midx = 0
			# find the nearest face
			for k in range(40 * 8):
				if z[k] < m:
					m = z[k]
					midx = k
			# predicted face index: midx // 8
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

# convert to numpy matrix
traindata = np.mat(traindata)
testdata = np.mat(testdata)

# feature scaling
mean_traindata = np.mean(traindata, 0)
for i in range(len(traindata)):
	traindata[i] = traindata[i] - mean_traindata
for i in range(len(testdata)):
	testdata[i] = testdata[i] - mean_traindata


# PCA eg. threshold = 0.9
u = PCA(traindata, testdata, 0.9)

# predict
traindata = traindata * u.T
testdata = testdata * u.T
predict(traindata, testdata)
		
