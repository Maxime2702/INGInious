#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def opposite(self):
        return Pair(-self.a, -self.b)