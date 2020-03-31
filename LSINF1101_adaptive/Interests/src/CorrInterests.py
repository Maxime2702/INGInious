#!/usr/bin/python3
# -*- coding: utf-8 -*-


def interests(base, rate, years):
    for i in range(1, years + 1):
        base += (base/100)*rate
    return base
