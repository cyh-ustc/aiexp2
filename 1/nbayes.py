#!/usr/bin/env python3
from tdm import tdm
import random


def nBayesClassifier(traindata, trainlabel, testdata, testlabel, threshold):
	# train
	wordspam = [0 for i in range(M)]
	wordham = [0 for i in range(M)]
	for i in range(len(traindata)):
		if trainlabel[i]:
			for j in traindata[i]:
				wordspam[j[0]] += 1
		else:
			for j in traindata[i]:
				wordham[j[0]] += 1
	
	probspam = [i / 400 for i in wordspam]
	probham = [i / 2000 for i in wordham]
	
	
	#print(wordspam, wordham)
	# 
	np2p = 0
	nn2p = 0
	ypred = []
	for i in range(len(testdata)):
		p1 = 1 #init probility
		p2 = 1
		
		for j in testdata[i][0]:
			if wordspam[j] and wordham[j]:
				p1 *= probspam[j]
				p2 *= probham[j]
		for j in testdata[i][1]:
			if wordspam[j] and wordham[j]:
				p1 *= (1 - probspam[j])
				p2 *= (1 - probham[j])
		p1 /= 6
		p2 *= (5/6)
		if p1 + p2 == 0.0:
			p = testlabel[i]
		else:
			p = p1 / (p1 + p2)
		

		if p > threshold:
			ypred.append(1)
			if testlabel[i]:
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

for idx in range(5):

	traindata = []
	trainlabel = []
	testdata = []
	testlabel = []
	u = set(range(M))
	for i in range(400):
		traindata.append(sn[x[i]])
		trainlabel.append(1)
	for i in range(100):
		tmpz = set([z[0] for z in sn[x[i + 400]]])
		testdata.append([tmpz, u - tmpz])
		testlabel.append(1)

	
	for i in range(2000):
		traindata.append(hn[y[i]])
		trainlabel.append(0)
	for i in range(500):
		tmpz = set([z[0] for z in hn[y[i + 2000]]])
		testdata.append([tmpz, u - tmpz])
		testlabel.append(0)

	print(nBayesClassifier(traindata, trainlabel, testdata, testlabel,0.5)[3])
	x =  x[100:] + x[:100]
	y =  y[500:] + y[:500]

