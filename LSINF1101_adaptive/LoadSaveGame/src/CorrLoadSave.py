#!/usr/bin/python3
# -*- coding: utf-8 -*-


def save_data(filename, life, mana, position_x, position_y):
    with open(filename, 'w') as f:
        f.write(str(life)+'\n')
        f.write(str(mana)+'\n')
        f.write(str(position_x)+'\n')
        f.write(str(position_y)+'\n')

def load_data(filename):
    try:
        f = open(filename, 'r')
        life = int(f.readline())
        mana = int(f.readline())
        position_x = int(f.readline())
        position_y = int(f.readline())
        return life, mana, position_x, position_y
    except FileNotFoundError:
        raise FileNotFoundError("file not found")
