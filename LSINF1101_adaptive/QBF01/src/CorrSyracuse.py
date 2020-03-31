#!/usr/bin/python3
# -*- coding: utf-8 -*-

# the student knows while and if
def syracuse(s0):
    si = s0
    while si != 1:
        print(si)
        if si % 2 == 0:
            si //= 2
        else:
            si = 3*si + 1
    print(si)
        