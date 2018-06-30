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

	m = dict()
	idx = 0
	for i in allwords:
		m[i] = idx
		idx += 1

	sn = []
	hn = []

	for i in spam:
		sn.append([])
		for j in i:
			sn[-1].append(tuple([m[j], i[j]]))

	for i in ham:
		hn.append([])
		for j in i:
			hn[-1].append(tuple([m[j], i[j]]))
		

	return sn, hn, len(allwords)