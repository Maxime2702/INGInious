#!/usr/bin/python3
# -*- coding: utf-8 -*-

# the student knows while and if
def qbf(n):
    for i in range (1, n+1):
        nb_div = 0
        for e in range(1, i):
            if i % e == 0:
                nb_div += 1
        print(i,':',nb_div)
        