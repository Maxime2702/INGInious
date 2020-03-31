#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fibonacci(n):
    if n < 0: return False
    elif n < 2: return n
    else: return fibonacci(n-1) + fibonacci(n-2)
