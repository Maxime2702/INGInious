#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFibonacci as corr
import fibonacci


class TestQuetelet(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(fibonacci, 'fibonacci'), _("You did not name the method as expected."))

    def test_factorial(self):
        a = [random.randint(1, 30) for _ in range(5)]
        ans = _("The {}th fibonacci number is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = fibonacci.fibonacci(a[i])
            corr_ans = corr.fibonacci(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_zero(self):
        ans = _("For 0 the fibonacci number is 0 and you returned {}.")
        stu_ans = fibonacci.fibonacci(0)
        self.assertEqual(0, stu_ans, ans.format(stu_ans))

    def test_one(self):
        ans = _("For 1 the fibonacci number is 1 and you returned {}.")
        stu_ans = fibonacci.fibonacci(1)
        self.assertEqual(1, stu_ans, ans.format(stu_ans))


if __name__ == '__main__':
    unittest.main()
