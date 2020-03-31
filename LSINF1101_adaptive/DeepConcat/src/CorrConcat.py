#!/usr/bin/python3
# -*- coding: utf-8 -*-


def deep_concat(l):
    if not l: return ""
    head, *tail = l
    if type(head) is list:
        return deep_concat(head + tail)
    else:
        return str(head) + deep_concat(tail)
