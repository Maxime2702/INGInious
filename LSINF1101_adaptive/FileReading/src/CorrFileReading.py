#!/usr/bin/python3
# -*- coding: utf-8 -*-


def line_count(filename):
    file = open ( filename, "r" )
    cnt = 0
    for line in file:
        cnt += 1
    file.close ()
    return cnt

def char_count(filename):
    file = open ( filename, "r" )
    cnt = 0
    for line in file:
        cnt += len(line)
    file.close ()
    return cnt

def space(filename,n):
    file = open ( filename, "w" )
    file.write ( " " * n )
    file.close ()

def capitalize(filename_in,filename_out):
    file_in = open ( filename_out, "r" )
    file_out = open ( filename_out, "w")
    for line in file_in:
        file_out.write ( line.upper () )
    file_in.close ()
    file_out.close ()

