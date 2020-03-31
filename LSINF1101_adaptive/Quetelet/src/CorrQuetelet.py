#!/usr/bin/python3
# -*- coding: utf-8 -*-


def quetelet(size, weight):
    index = weight/(size*size)
    if index < 20: return "thin"
    elif index <= 25: return "normal"
    elif index <= 30: return "overweight"
    else: return "obese"
