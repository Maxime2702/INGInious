#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os

def files(path):
    res = []
    it = os.scandir(path)
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            res.append(entry.name)
    return res

def directories(path):
    res = []
    it = os.scandir(path)
    for entry in it:
        if entry.is_dir():
            res.append(entry.name)
    return res
    
def subfiles(directory):
    res = []
    it = os.scandir(directory)
    for entry in it:
        if entry.is_dir():
            new_path = os.path.join(directory, entry.name)
            it2 = os.scandir(new_path)
            for entry2 in it2:
                if entry2.is_file():
                    res.append(os.path.join(new_path, entry2.name))
    return res
                      
