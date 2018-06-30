#!/usr/bin/env python3
from tdm import tdm
import random


def nBayesClassifier(traindata, trainlabel, testdata, testlabel, threshold):
	# train
	wordspam = [0 for i in range(32000)]
	wordham = [0 for i in range(32000)]
	for i in range(len(traindata)):
		if trainlabel[i]:
			for j in traindata[i]:
				wordspam[j[0]] += 1
		else:
			for j in traindata[i]:
				wordham[j[0]] += 1
	
	probspam = [i / 450 for i in wordspam]
	probham = [i / 2250 for i in wordham]
	
	
	#print(wordspam, wordham)
	# 
	np2p = 0
	nn2p = 0
	
	for i in range(len(testdata)):
		p1 = 1 #init probility
		p2 = 1
		
		for j in testdata[i][0]:
			if wordspam[j] and wordham[j]:
				p1 *= probspam[j]
				p2 *= probham[j]
		print(p1, p2)
		for j in testdata[i][1]:
			if wordspam[j] and wordham[j]:
				p1 *= (1 - probspam[j])
				p2 *= (1 - probham[j])
		p1 /= 6
		p2 *= (5/6)
		print(p1, p2)
		p = p1 / (p1 + p2)
		
		
		print(p)
		if p > threshold:
			if testlabel[i]:
				np2p += 1
			else:
				nn2p += 1
	print(nn2p, np2p)
	SP = np2p / (np2p + nn2p) 
	SR = np2p / 50
	F = SP * SR * 2 / (SP + SR)
	return SP, SR, F

sn, hn, M = tdm()

traindata = []
trainlabel = []
testdata = []
testlabel = []
u = set(range(M))

x = list(range(500))
random.shuffle(x)
for i in range(450):
	traindata.append(sn[x[i]])
	trainlabel.append(1)
for i in range(50):
	tmpz = set([z[0] for z in sn[x[i + 450]]])
	testdata.append([tmpz, u - tmpz])
	testlabel.append(1)

x = list(range(2551))
random.shuffle(x)
for i in range(2250):
	traindata.append(hn[x[i]])
	trainlabel.append(0)
for i in range(250):
	tmpz = set([z[0] for z in hn[x[i + 2250]]])
	testdata.append([tmpz, u - tmpz])
	testlabel.append(0)

print(nBayesClassifier(traindata, trainlabel, testdata, testlabel, 0.5))


