#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fun_repetition(f, n):
    def repeat(x):
        acc = x
        for _ in range(n):
            acc = f(acc)
        return acc
    return repeat

