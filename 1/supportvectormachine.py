#!/usr/bin/env python3
from tdm import tdm
import numpy as np
import random
import SVM


def softsvm(traindata, trainlabel, testdata, testlabel, sigma, C):
	if sigma == 0:
		kernel_type='linear'
	else:
		kernel_type='quadratic'
	model = SVM.SVM(kernel_type, C, sigma)
	model.fit(traindata, trainlabel)
	result = model.predict(testdata)
	# print(result)
	ypred = []
	np2p = 0
	nn2p = 0
	for i in range(300):
		if result[i] == 1:
			ypred.append(1)
			if testlabel[i] == 1:
				np2p += 1
			else:
				nn2p += 1
		else:
			ypred.append(0)
	#print(nn2p, np2p)
	SP = np2p / (np2p + nn2p) 
	SR = np2p / 50
	F = SP * SR * 2 / (SP + SR)
	print(ypred, SP, SR, F)
	
# load data
sn, hn, M = tdm()

traindata = []
trainlabel = []
testdata = []
testlabel = []

# select traindata & testdata

# sparse matrix -> matrix

x = list(range(500))
random.shuffle(x)
for i in range(450):
	traindata.append([0 for j in range(M)])
	for j in sn[x[i]]:
		traindata[-1][j[0]] = j[1]
for i in range(50):
	testdata.append([0 for j in range(M)])
	for j in sn[x[i + 450]]:
		testdata[-1][j[0]] = j[1]

x = list(range(2500))
random.shuffle(x)
for i in range(2250):
	traindata.append([0 for j in range(M)])
	for j in hn[x[i]]:
		traindata[-1][j[0]] = j[1]
for i in range(250):
	testdata.append([0 for j in range(M)])
	for j in hn[x[i + 2250]]:
		testdata[-1][j[0]] = j[1]

# create label matrix(array) 1(spam) or -1(ham)
		
trainlabel =[1 for i in range(450)] + [-1 for i in range(2250)]
testlabel = [1 for i in range(50)] + [-1 for i in range(250)]

# use numpy array

traindata = np.array(traindata)
trainlabel = np.array(trainlabel)
testdata = np.array(testdata)
testlabel = np.array(testlabel)

# svm

softsvm(traindata, trainlabel, testdata, testlabel, 0, 25)