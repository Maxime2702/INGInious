#! /usr/bin/python3
# -*- coding: utf-8 -*-

def fibo(n):
    if n < 0: return False
    elif n < 2: return n
    else: return fibo(n-1) + fibo(n-2)
    
def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        fa = 0
        fb = 1
        for i in range(n-1) :
            fn = fb + fa
            fa = fb
            fb = fn
        return fn  

def fibo_mem(n):
    if n <= 1:
        return n
    else:
        return memoization(fibo_mem, n-1) + memoization(fibo_mem, n-2)

def fact_mem(n):
    if n == 0:
        return 1
    else:
        return n * memoization(fact_mem, n-1)

def n_sum_mem(n):
    if n < 2:
        return n
    else:
        return n + memoization(n_sum_mem, n-1)

fibo_dict = { }
fact_dict = { }
sum_dict = { }

mapping = {fibo_mem: fibo_dict, fact_mem: fact_dict, n_sum_mem: sum_dict}

def memoization(fun, n):
    if n in mapping[fun]: return mapping[fun][n]
    else:
        mapping[fun][n] = fun(n)
        return mapping[fun][n]
