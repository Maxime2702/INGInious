#!/usr/bin/python3
# -*- coding: utf-8 -*-

def compute_sum_even(matrix):
    sum_even = 0

    iterator_lines = iter(matrix)
    while True:
        try:
            line = next(iterator_lines)
            iterator_elem = iter(line)
            while True:
                try:
                    elem = next(iterator_elem)
                    if elem % 2 == 0:
                        sum_even += elem
                except (StopIteration, RuntimeError):
                    break
        except (StopIteration, RuntimeError):
            break

    return sum_even
