#!/usr/bin/python3
# -*- coding: utf-8 -*-


def binary_search(course, list_of_courses):
	first = 0
	last = len(list_of_courses)-1
	found = False

	while first<=last and not found:
		middle = (first + last)//2
		course_name, students = list_of_courses[middle]
		if course_name == course:
			found = True
		else:
			if course < course_name:
				last = middle-1
			else:
				first = middle+1

	if found:
		return students
	else:
		return []
