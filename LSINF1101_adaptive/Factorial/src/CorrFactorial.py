#!/usr/bin/python3
# -*- coding: utf-8 -*-


def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    else:
        return False