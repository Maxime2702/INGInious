#!/usr/bin/python3
# -*- coding: utf-8 -*-


def write(file, name):
    try:
        with open(file, 'r+') as f:
            letter = f.read()
            edited_letter = letter.replace('#', name)
            f.seek(0)
            f.write(edited_letter)
    except IOError:
        raise IOError("File does not exist.")
