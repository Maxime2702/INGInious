#!/usr/bin/python3
# -*- coding: utf-8 -*-


def average(list):
    if len(list) == 0: return None
    sum = 0
    for e in list:
        sum += e
    return sum/len(list)