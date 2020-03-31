#!/usr/bin/python3
# -*- coding: utf-8 -*-


def accumulate(e, f, l):
    if l:
        return accumulate(f(e, l[0]), f, l[1:])
    else:
        return e	

def sum(l): 
    return accumulate(0, lambda a, b : a + b, l)
def mul(l): 
    return accumulate(1, lambda a, b : a * b, l)
def max(l): 
    return accumulate(l[0], lambda a, b : a if a > b else b, l)
def concat(l): 
    return accumulate('', lambda a, b : str(a) + str(b), l)
