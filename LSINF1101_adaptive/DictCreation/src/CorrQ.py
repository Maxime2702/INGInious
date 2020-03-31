#!/usr/bin/python3
# -*- coding: utf-8 -*-


def create_dict(l):
	d = {}
	for x, y in l:
		if x not in d:
			d[x] = [y]
		else:
			d[x].append ( y )
	return d
