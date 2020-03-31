#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Student:
	def __init__(self, firstname, surname, mark):
		self.firstname = firstname
		self.surname = surname
		self.mark = mark

	def __eq__(self, s):
		return self.firstname == s.firstname and self.surname == s.surname and self.mark == s.mark

	def __repr__(self):
		return "{}, {}: {}".format(self.surname, self.firstname, self.mark)

	def __str__(self):
		return "{}, {}: {}".format(self.surname, self.firstname, self.mark)

def marks_from_file(filename):
	res = []
	with open(filename) as file:
		for line in file:
			tab = line.split()
			student = Student(tab[0], tab[1], int(tab[2]))
			res.append(student)
	return res
