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
	
	
	p = [i[0] for i in predicty]
	p1 = p[:50]
	p2 = p[50:]
	p1.sort()
	mf = 50
	mt = 0
	for i in range(len(p1)):
		m2 = 0
		for j in p2:
			if j > p1[i]:
				m2 += 1
		f = (50 + m2)/(50 - i + 1)
		if f < mf:
			mf = f
			mt = p1[i]
	
	np2p = 0
	nn2p = 0
	ypred = []
	for i in range(len(p)):
		if p[i] > mt:
			ypred.append(1)
			if testlabel[0, i]:
				np2p += 1
			else:
				nn2p += 1
		else:
			ypred.append(0)
	#print(nn2p, np2p)
	SP = np2p / (np2p + nn2p) 
	SR = np2p / 50
	F = SP * SR * 2 / (SP + SR)
	return ypred, SP, SR, F
	

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


print(lsClassifier(traindata, trainlabel, testdata, testlabel, 1))