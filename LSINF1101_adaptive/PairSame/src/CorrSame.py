#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __eq__(self, p):
        if p is not None:
            return self.a == p.a and self.b == p.b
        else:
            return False

