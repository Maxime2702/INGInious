#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return "{}, {}".format(self.a, self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def opposite(self):
        return Pair(-self.a, -self.b)

class OrderedPair:
    def __init__(self):
        self.p = Pair(0, 0)
        self.ordered = True

    def set_a(self, n_a):
        self.p.a = n_a
        self.ordered = (True if self.p.a <= self.p.b else False)

    def set_b(self, n_b):
        self.p.b = n_b
        self.ordered = (True if self.p.a <= self.p.b else False)

