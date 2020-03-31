#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import re

import CorrWrongIterations as corr
import wrongIterations as stu

def gen_random_matrix():
    matrix = []

    max_size = 10
    max_elem_abs = 100

    nb_lines = random.randint(1, max_size)
    nb_cols = random.randint(1, max_size)
    for i in range(nb_lines):
        matrix.append([])
        for j in range(nb_cols):
            matrix[i].append(random.randint(-max_elem_abs, max_elem_abs))

    return matrix

regex_for = re.compile(r"\bfor\b")

def contains_for_loop(code):
    return re.search(regex_for, code)


class TestWrongIter(unittest.TestCase):
    def test_random(self):
        # Check if there is a for loop in student's answer
        with open("wrongIterations.py", "r") as student_code:
            if contains_for_loop(student_code.read()):
                self.fail(_("Well tried! But you cannot use a `for` loop in this exercise. Use `while` and iterators "
                            "instead."))
            else:
                # Check answer
                for i in range(15):
                    matrix = gen_random_matrix()
                    correct_ans = corr.compute_sum_even(matrix)
                    try:
                        student_ans = stu.compute_sum_even(matrix)
                    except Exception as e:
                        self.fail(_("Your code raised an exception ({}('{}')) while handling matrix "
                                    "{}.".format(type(e).__name__, e, matrix)))
                    self.assertEqual(correct_ans, student_ans, _("With matrix {}, you computed an incorrect sum of "
                                                                 "even numbers {} instead of {}.".format(matrix,
                                                                                                         student_ans,
                                                                                                         correct_ans)))


if __name__ == '__main__':
    unittest.main()
