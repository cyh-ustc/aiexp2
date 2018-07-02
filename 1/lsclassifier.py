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
	p1 = p[:100]
	p2 = p[100:]
	p1.sort()
	mf = 100
	mt = 0
	for i in range(len(p1)):
		m2 = 0
		for j in p2:
			if j > p1[i]:
				m2 += 1
		f = (100 + m2)/(100 - i + 1)
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
	SR = np2p / 100
	F = SP * SR * 2 / (SP + SR)
	return ypred, SP, SR, F
	

sn, hn, M = tdm()

x = list(range(500))
random.shuffle(x)
y = list(range(2500))
random.shuffle(y)

# 5 cross validation
f = []
for idx in range(5):

	traindata = []
	trainlabel = []
	testdata = []
	testlabel = []

	for i in range(400):
		traindata.append([0 for j in range(M)])
		for j in sn[x[i]]:
			traindata[-1][j[0]] = j[1]
	for i in range(100):
		testdata.append([0 for j in range(M)])
		for j in sn[x[i + 400]]:
			testdata[-1][j[0]] = j[1]

	for i in range(2000):
		traindata.append([0 for j in range(M)])
		for j in hn[y[i]]:
			traindata[-1][j[0]] = j[1]
	for i in range(500):
		testdata.append([0 for j in range(M)])
		for j in hn[y[i + 2000]]:
			testdata[-1][j[0]] = j[1]

	traindata = np.mat(traindata)
	testdata = np.mat(testdata)
	trainlabel = np.mat([1 for i in range(400)] + [0 for i in range(2000)])
	testlabel = np.mat([1 for i in range(100)] + [0 for i in range(500)])


	f.append(lsClassifier(traindata, trainlabel, testdata, testlabel,1000)[3])
	x =  x[100:] + x[:100]
	y =  y[500:] + y[:500]
print(f)
print(sum(f)/len(f))


