#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fizz_buzz(i):
    tmp = ""
    if i % 3 == 0: tmp += "fizz"
    if i % 5 == 0: tmp += "buzz"
    if not i % 5 == 0 and not i% 3 == 0: return "no"
    return tmp