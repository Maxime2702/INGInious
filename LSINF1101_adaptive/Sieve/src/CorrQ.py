#!/usr/bin/python3
# -*- coding: utf-8 -*-


from math import sqrt

def sieve(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = sieve(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p
