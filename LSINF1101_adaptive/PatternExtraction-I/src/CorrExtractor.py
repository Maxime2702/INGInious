#!/usr/bin/python3
# -*- coding: utf-8 -*-


def extract(code):
    pattern = ""
    for c in code:
        if c.isdigit(): pattern += "number "
        elif c.lower() in "aeiouy":
            if c.isupper(): pattern += "vowel-up "
            else: pattern += "vowel-low "
        else:
            if c.isupper(): pattern += "consonant-up "
            else: pattern += "consonant-low "
    return pattern[:-1]
