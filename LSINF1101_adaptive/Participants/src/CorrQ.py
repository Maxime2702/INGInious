#!/usr/bin/python3
# -*- coding: utf-8 -*-


def students(course, student_courses):
    return [ s for (s,c) in student_courses if c == course]
