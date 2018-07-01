#!/usr/bin/env python3
from tdm import tdm
import numpy as np
import random

def lsClassifier(traindata, trainlabel, testdata, testlabel, _lambda):
	x = traindata
	y = trainlabel
	z = x.T * x

	omega = (z + _lambda*np.eye(z.shape[0])).I * x.T * y.T
	predicty =  testdata * omega
	print(predicty)
	
	






sn, hn, M = tdm()

traindata = []
trainlabel = []
testdata = []
testlabel = []

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

traindata = np.mat(traindata)
testdata = np.mat(testdata)
trainlabel = np.mat([1 for i in range(450)] + [0 for i in range(2250)])
testlabel = np.mat([1 for i in range(50)] + [0 for i in range(250)])


lsClassifier(traindata, trainlabel, testdata, testlabel, 0.1)