#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Counters:
    def __init__ ( self, number ):
        self.counters = {}
        for i in range(number):
            self.counters[i] = 0

    def next(self, number):
        if number not in self.counters:
            raise IndexError ( "Counter does not exist" )
        val = self.counters[number]
        self.counters[number] += 1
        return val
