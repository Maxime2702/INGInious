#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, next_node, value):
        self.next_node = next_node
        self.value = value

    def get_next(self):
        return self.next_node

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(None, value)
        else:
            self.root = Node(self.root, value)

    def get_reverse(self):
        res = ""
        node = self.root
        while node is not None:
            res += str(node.get_value())
            node = node.get_next()
        return res
