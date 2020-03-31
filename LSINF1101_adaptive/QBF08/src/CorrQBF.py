#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fib(n):
    dejacalcule = {0: 0, 1: 1}
    def fib_mem(n):
        if n not in dejacalcule:
            new_value = fib_mem(n-1) + fib_mem(n-2)
            dejacalcule[n] = new_value
        return dejacalcule[n]
    return fib_mem(n)
