#!/usr/bin/env python3
import numpy as np
def loadpgm(path):
	f = open(path, 'rb')
	f.read(0xd)
	return list(f.read(92 * 112))



# load data
traindata = []
for i in range(40):#40 persons
	for j in range(10):
		traindata.append(loadpgm('faces/s%d/%d.pgm'%(i + 1, j + 1)))


