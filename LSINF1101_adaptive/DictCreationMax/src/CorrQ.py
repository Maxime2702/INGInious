#!/usr/bin/python3
# -*- coding: utf-8 -*-


def create_dict_max(l):
	d = {}
	for x, y in l:
		if x not in d:
			d[x] = y
		else:
			if y >= d[x]:
				d[x] = y
	return d
