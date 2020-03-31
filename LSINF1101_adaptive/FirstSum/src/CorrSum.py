#!/usr/bin/python3
# -*- coding: utf-8 -*-


def sum(n):
    if n >= 0:
        if n == 1:
            return 1
        else:
            return n + sum(n-1)
    else:
        return False