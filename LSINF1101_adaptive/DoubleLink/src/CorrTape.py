#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, s):
        self.s = s
        self.next_node = None
        self.previous_node = None

    def set_next(self, next_node):
        self.next_node = next_node

    def set_previous(self, previous_node):
        self.previous_node = previous_node

    def get_next(self):
        return self.next_node

    def get_previous(self):
        return self.previous_node

    def get_text(self):
        return self.s

    def set_text(self, s):
        self.s = s

class Tape:
    def __init__(self):
        self.actual = None
        self.last = None
        self.length = 0
        
    def next(self):
        if self.actual is not None and self.actual.get_next() is not None:
            self.actual = self.actual.get_next()
            return self.actual.get_text()
        return None
        
    def previous(self):
        if self.actual is not None and self.actual.get_previous() is not None:
            self.actual = self.actual.get_previous()
            return self.actual.get_text()
        return None
    
    def get_length(self):
        return self.length
        
    def add(self, s):
        n = Node(s)
        if self.actual is None:
            self.actual = n
            self.last = n
            self.length = 1
        else:
            n.set_previous(self.last)
            self.last.set_next(n)
            self.last = n
            self.length += 1
        
    def write(self, s):
        if self.actual is not None:
            self.actual.set_text(s)
            
    def read(self):
        if self.actual is not None:
            return self.actual.get_text()
        return None
