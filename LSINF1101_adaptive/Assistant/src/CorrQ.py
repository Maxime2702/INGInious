#!/usr/bin/python3
# -*- coding: utf-8 -*-

def asked_fun(fun):
    return { 'square': lambda x: x**2, 'mul3': lambda x: x*3, 'add2': lambda x: x+2}[fun]
