#!/usr/bin/python3
# -*- coding: utf-8 -*-


def count(events,i,j):
	cnt = 0
	for e in events:
		if e == (i,j):
			cnt += 1
	return cnt
