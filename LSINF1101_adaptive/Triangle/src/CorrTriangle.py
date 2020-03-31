#!/usr/bin/python3
# -*- coding: utf-8 -*-


def triangle(n):
    l = []
    for i in range(1,n+2):
        l.append ( list ( range ( i ) ) )
    return l