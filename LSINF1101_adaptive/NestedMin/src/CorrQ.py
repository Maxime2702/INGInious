#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def recursive_min(l):
    res = sys.maxsize 
    for e in l:
        if type(e) is list:
            res = min(res, recursive_min(e))
        else:
            res = min(res, e)
    return res
