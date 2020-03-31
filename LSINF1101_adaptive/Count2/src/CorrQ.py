#!/usr/bin/python3
# -*- coding: utf-8 -*-


def count(events,i,j):
	cnt = 0
	for e in events:
		if e == (i,j):
			cnt += 1
	return cnt

def counts(events,n,m):
	matrix = [ [0 for i in range(m) ] for j in range(n) ]
	for i in range(0,n):
		for j in range(0,m):
			matrix[i][j] = matrix[i][j] + count ( events, i, j )
	return matrix