#!/usr/bin/python3
# -*- coding: utf-8 -*-

def sort_courses(student_courses):
	courses_students = []
	for student, course in student_courses:
		courses_students.append((course, student))
	return sorted(courses_students)

def nest_students(student_courses):
	l = []
	name = None
	for (course,student) in sort_courses(student_courses):
		if course != name:
			sl = [student]
			l.append((course, sl))
			name = course
		else:
			sl.append(student)
	return l
