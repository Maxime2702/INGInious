#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Student:

    student_number = 0

    def __init__(self, name, surname, birth_date, email):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.email = email
        self.courses = {}
        self. num = Student.student_number
        Student.student_number += 1

    def __str__(self):
        ans = _("Student number {}: {} {} born the {}, can be reached at {}")
        return ans.format(self.num, self.name, self.surname, self.birth_date, self.email)