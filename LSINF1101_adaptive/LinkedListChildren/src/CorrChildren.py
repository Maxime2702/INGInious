#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Child:
    def __init__(self):
        self.next = None

    def is_next_valid(self):
        return self.next is not None

    def next_child(self):
        return self.next


def is_every_child_here(first_child):
    head = first_child
    pointer = first_child
    while pointer.is_next_valid():
        if pointer.next_child() == head:
            return True
        pointer = pointer.next_child()
    return False
