#!/usr/bin/python3
# -*- coding: utf-8 -*-


def extract(code):
    pattern = ""
    for c in code:
        if c.isdigit(): pattern += "number "
        elif c in "aeiouy":
            if c.isupper(): pattern += "vowel-up "
            else: pattern += "vowel-low "
        else:
            if c.isupper(): pattern += "consonant-up "
            else: pattern += "consonant-low "
    return pattern

def treatment(data):
    pattern = ""
    current = data.split()[0]
    count = 0
    for c in data.split():
        if c == current:
            count += 1
        else:
            pattern += current + '*' + str(count) + ' '
            count = 1
            current = c
    return pattern

def collect(file):
    dic = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                pat = treatment(extract(line))
                if pat in dic: dic[pat] += 1
                else: dic[pat] = 1
    except IOError:
        raise IOError("File does note exist.")
    return dic
