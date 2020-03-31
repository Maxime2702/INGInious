#!/usr/bin/python3
# -*- coding: utf-8 -*-


def count(lst):
    lt = []
    for e in lst:
        if e not in lt:
            lt += [e]
    return len(lt)
