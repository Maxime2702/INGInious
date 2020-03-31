#!/usr/bin/python3
# -*- coding: utf-8 -*-


def gd(a):
    for i in range(a//2, 0, -1):
        if a % i == 0:
            return i
    return None
