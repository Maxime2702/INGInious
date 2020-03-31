#!/usr/bin/python3
# -*- coding: utf-8 -*-


def write_coordinates(filename,l):
	file = open(filename,"w")
	file.write('\n'.join("{0},{1}".format (x,y) for x, y in l))
	file.close()

def read_coordinates(filename):
	l = []
	file = open(filename,"r")
	for line in file:
		x, y = line.split(",")
		l.append((float(x),  float(y)))
	return l

