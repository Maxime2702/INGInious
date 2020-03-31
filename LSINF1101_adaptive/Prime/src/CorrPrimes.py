#!/usr/bin/python3
# -*- coding: utf-8 -*-


def prime(n):
    status = True
    for i in range(2, n):
        if n % i == 0:
            status = False

    return status
