#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import string
import random
import unicodedata

import CorrStudent as corr
import student


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestStudent(unittest.TestCase):
    def test_exist(self):
        self.assertTrue((hasattr(student.Student, '__init__') and hasattr(student.Student, '__str__')),
                        _("You did not provide the init or str methods."))

    def test_str(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        surname = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        birthdate = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        ans = _("With the following data: {}, {}, {}, {} for the student created, you returned {} instead of {}")
        stu_ans = student.Student(name, surname, birthdate, email)
        corr_ans = corr.Student(name, surname, birthdate, email)
        self.assertEqual(equal_string(str(corr_ans)), equal_string(str(stu_ans)), ans.format(name, surname, birthdate,
                                                                                             email, stu_ans, corr_ans))

    def test_multi_student(self):
        names = [''.join(random.choice(string.ascii_letters) for _ in range(8)) for _ in range(5)]
        surnames = [''.join(random.choice(string.ascii_letters) for _ in range(8)) for _ in range(5)]
        birthdates = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) for _ in range(5)]
        emails = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) for _ in range(5)]
        ans = _("With the following data: {}, {}, {}, {} for the {}th student created, you returned {} instead of {}")
        for i in range(len(names)):
            stu_ans = student.Student(names[i], surnames[i], birthdates[i], emails[i])
            corr_ans = corr.Student(names[i], surnames[i], birthdates[i], emails[i])
            self.assertEqual(equal_string(str(corr_ans)), equal_string(str(stu_ans)), ans.format(names[i], surnames[i],
                                                                                                 birthdates[i],
                                                                                                 emails[i], i, stu_ans,
                                                                                                 corr_ans))
    def test(self):
        for e in dir(student):
            if not e.endswith('__') and e != 'Student':
                self.fail("Vous utilisez une variable globale ce qui est déconseillé; essayez d’adapter votre exercice afin d’utiliser une variable de classe au lieu d’une variable globale")


if __name__ == '__main__':
    unittest.main()
