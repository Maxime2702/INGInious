#!/usr/bin/python3
# -*- coding: utf-8 -*-


def plus_frequent(l):
    dic = {}
    for e in l:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 0
    return max(dic, key=dic.get)
