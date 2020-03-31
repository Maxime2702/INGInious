#! /usr/bin/python3
# -*- coding: utf-8 -*-

def squares1():
    n = 1
    s = 0
    while n <= 10:
        c = n*n
        s = s + c
        print(n, "\t", c, "\t", s)
        n = n+1

def squares2():
    s = 0
    for n in range(1,11):
        c = n*n
        s = s + c
        r = n * (n+1) * (n+n+1) // 6
        print(n, "\t", c, "\t", s, "\t", r)