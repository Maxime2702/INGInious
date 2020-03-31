#! /usr/bin/python3
# -*- coding: utf-8 -*-

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string


def readfile(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


def get_words(line):
    return ''.join(c.lower() for c in line if c not in string.punctuation).split()


def create_index(filename):
    lines = readfile(filename)
    dic = {}
    for i, line in enumerate(lines):
        for word in get_words(line):
            dic[word] = dic.get(word, {})
            dic[word][i] = dic[word].get(i, 0) + 1
    return dic


def get_lines(words, index):
    try:
        res = index[words[0]].keys()
        for word in words[1:]:
            res = [e for e in res if e in index[word].keys()]
    except KeyError:
        res = []
    return res
