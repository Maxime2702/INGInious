#!/usr/bin/python3
# -*- coding: utf-8 -*-

def mult_table(n):
    x=[]
    for i in range(n+1):
        x.append(lambda j,l=i: l*j)
    return x