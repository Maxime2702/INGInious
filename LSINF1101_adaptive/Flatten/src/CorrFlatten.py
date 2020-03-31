#!/usr/bin/python3
# -*- coding: utf-8 -*-


def flatten(l):
    res = []
    for e in l:
        if type(e) is list:
            res.extend(flatten(e))
        else:
            res.append(e)
    return res
