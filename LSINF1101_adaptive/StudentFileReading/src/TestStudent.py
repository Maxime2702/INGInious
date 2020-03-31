#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import string
import random

import CorrStudent as corr
import student


class TestStudent(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(student, 'marks_from_file'), _("Vous n'avez pas fourni la méthode marks_from_file"))

    def test_multi_student(self):
        names = [''.join(random.choice(string.ascii_letters) for _ in range(8)) for _ in range(5)]
        surnames = [''.join(random.choice(string.ascii_letters) for _ in range(8)) for _ in range(5)]
        marks = [''.join(str(random.randint(0,20)) for _ in range(8)) for _ in range(5)]
        ans = "Votre programme retourne {} au lieu de {}. Les étudiants ne seront pas contents que vous perdiez leurs points."
        with open('student.txt', 'w') as f:
            for i in range(len(names)):
                f.write('{} {} {}\n'.format(names[i], surnames[i], marks[i]))
        
        corr_ans = corr.marks_from_file('student.txt')
        stu_ans = student.marks_from_file('student.txt')
        if not isinstance(stu_ans[0], student.Student):  
            self.fail("Vous ne renvoyez pas une liste d'objets Student.")
        self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))

    def test_IOError(self):
        self.assertRaises(IOError, student.marks_from_file, 'IOError.txt')


if __name__ == '__main__':
    unittest.main()
