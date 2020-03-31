#!/usr/bin/python3
# -*- coding: utf-8 -*-

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)