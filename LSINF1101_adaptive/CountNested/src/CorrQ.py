#!/usr/bin/python3
# -*- coding: utf-8 -*-


def count(n, l):
    res = 0
    for e in l:
        if type(e) is list:
            res += count(n, e)
        elif e == n:
            res += 1
    return res
