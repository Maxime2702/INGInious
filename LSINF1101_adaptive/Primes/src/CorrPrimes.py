#!/usr/bin/python3
# -*- coding: utf-8 -*-


def primes(max):
    prime = []
    for i in range(2, max + 1):
        status = True
        for n in prime:
            if i % n == 0:
                status = False
        if status: prime.append(i)

    return prime
