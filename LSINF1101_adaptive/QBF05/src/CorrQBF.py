#!/usr/bin/python3
# -*- coding: utf-8 -*-


import math

def absolute(v1, v2):
	return math.fabs(v1 - v2)

def seatch_time(l, t):
	for i, e in enumerate(l):
		if e[0] >= t:
			return i
	return len(l)


def euclidian_distance(c1,c2):
	return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def cross(t1, t2, theta_1, theta_2):
	for time1, coord1 in t1:
		for time2, coord2 in t2:
			if absolute(time1, time2) <= theta_1 and euclidian_distance(coord1, coord2) < theta_2:
				return 1
	return 0

def matrix_for_traces(l, theta_1, theta_2):
	return [[cross(t1, t2, theta_1, theta_2) for t2 in l] for t1 in l]

