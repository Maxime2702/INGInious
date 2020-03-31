#!/usr/bin/python3
# -*- coding: utf-8 -*-

def merge(first_list, second_list):
    li = []
    i, j = 0, 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i][1] < second_list[j][1]:
            li.append(first_list[i])
            i += 1
        else:
            li.append(second_list[j])
            j += 1
    if i < len(first_list):
        li.extend(first_list[i:])
    if j < len(second_list):
        li.extend(second_list[j:])
    return li