#!/usr/bin/python3
# -*- coding: utf-8 -*-


def treatment(data):
    pattern = ""
    inp = data.split()
    current = inp[0]
    count = 0
    for i in range(len(inp)):
        if inp[i] == current and i < len(inp):
            count += 1
        else:
            pattern += current + '*' + str(count) + ' '
            count = 1
            current = inp[i]
    pattern += current + '*' + str(count)
    return pattern
