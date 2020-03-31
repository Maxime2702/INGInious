#!/usr/bin/python3
# -*- coding: utf-8 -*-


def create_dictionary(name):
    d = {}
    with open(name, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                d[word] = d.get(word, 0) + 1
    return d

def occ(d, w):
    return d.get(w, 0)

