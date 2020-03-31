#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Button:
    def __init__(self, size, label, callback):
        self.set_size(size)
        self.set_label(label)
        self.on_click(callback)

    def set_size(self, new_size):
        if type(new_size) != tuple:
            raise ValueError("Tried to set size to invalid value")
        if len(new_size) != 2:
            raise ValueError("Invalid number of elements when trying to set size")
        if type(new_size[0]) != int or type(new_size[1]) != int:
            raise ValueError("Tried to set size to non-integer values")
        if new_size[0] < 0 or new_size[1] < 0:
            raise ValueError("Tried to set size to negative values")
        self.size = new_size

    def set_label(self, new_label):
        if type(new_label) != str:
            raise ValueError("Tried to set label to invalid value")
        self.label = new_label

    def on_click(self, new_callback):
        if not callable(new_callback):
            raise ValueError("Tried to set callback to invalid value")
        self.callback = new_callback

    def clicked(self):
        return self.callback()

    def __str__(self):
        return "Button {{ size:({},{}), label:'{}', callback:'{}' }}".format(
            self.size[0], self.size[1], self.label, self.callback.__name__)
