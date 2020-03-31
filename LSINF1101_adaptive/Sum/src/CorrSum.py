#!/usr/bin/python3
# -*- coding: utf-8 -*-


def sum(list):
    sum = 0
    for e in list:
        if type(e) is int or type(e) is float:
            sum += e
    return sum
