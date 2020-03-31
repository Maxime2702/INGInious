#!/usr/bin/python3
# -*- coding: utf-8 -*-


fibo = {}
fact = {}
sum_dic = {}

def n_sum(n):
    if n < 2:
        return n
    else:
        return n + memoization(n_sum, n-1)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return memoization(fibonacci, n-1) + memoization(fibonacci, n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * memoization(factorial, n-1)

mapping = {fibonacci: fibo, factorial: fact, n_sum: sum_dic}
def memoization(fun, n):
    if n in mapping[fun]: return mapping[fun][n]
    else:
        mapping[fun][n] = fun(n)
        return mapping[fun][n]