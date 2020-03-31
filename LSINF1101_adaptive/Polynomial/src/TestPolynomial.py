#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrPolynomial as corr
import polynomial as stu


class TestPolynomial(unittest.TestCase):
    def test_random(self):
        lower_bound = -100.0
        higher_bound = 100.0
        for i in range(15):
            a = random.uniform(lower_bound, higher_bound)
            b = random.uniform(lower_bound, higher_bound)
            c = random.uniform(lower_bound, higher_bound)
            x = random.uniform(lower_bound, higher_bound)
            correct_ans = corr.polynomial(a, b, c, x)
            student_ans = stu.polynomial(a, b, c, x)
            self.assertAlmostEqual(correct_ans, student_ans, places = 0, msg = _("With a={}, b={}, c={} and x={}, your code computes {} instead of {}.").format(str(a), str(b), str(c), str(x), str(student_ans), str(correct_ans)))


if __name__ == '__main__':
    unittest.main()
