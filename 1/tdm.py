#!/usr/bin/env python3
def tdm():
	spam = []
	ham = []

	allwords = set()


	for i in range(500):
		spam.append(dict())
		f = open('spam/%04d'%(i+1), 'rt')
		z = f.read()
		m = z.split(' ')
		for j in m:
			allwords.add(j)
			if j in spam[-1]:
				spam[-1][j] += 1
			else:
				spam[-1][j] = 1
		f.close()

	for i in range(2551):
		ham.append(dict())
		f = open('ham/%04d'%(i+1), 'rt')
		z = f.read()
		m = z.split(' ')
		for j in m:
			allwords.add(j)
			if j in ham[-1]:
				ham[-1][j] += 1
			else:
				ham[-1][j] = 1
		f.close()

	
	z = dict()
	for i in allwords:
		z[i] = [0, 0]

	
	for i in spam:
		for j in i:
			z[j][0] += 1
	for i in ham:
		for j in i:
			z[j][1] += 1
	
	upper = 0.9
	lower = 0.03
	
	selectwords = dict()
	idx = 0
	for i in z:
		if(z[i][0] >= 500 * lower and z[i][1] >= 2500 * lower and z[i][0] <= 500 * upper and z[i][1] <= 2500 * upper):
			selectwords[i] = idx
			idx += 1


	sn = []
	hn = []

	for i in spam:
		sn.append([])
		for j in i:
			if  j in selectwords:
				sn[-1].append(tuple([selectwords[j], i[j]]))

	for i in ham:
		hn.append([])
		for j in i:
			if  j in selectwords:
				hn[-1].append(tuple([selectwords[j], i[j]]))
		

	return sn, hn, len(selectwords)