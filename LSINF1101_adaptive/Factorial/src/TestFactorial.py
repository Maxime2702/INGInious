#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFactorial as corr
import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        a = [random.randint(1, 100) for _ in range(5)]
        ans = _("The factorial of the integer {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = factorial.factorial(a[i])
            corr_ans = corr.factorial(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_zero(self):
        ans = _("The factorial of 0 is 1 and you returned {}.")
        stu_ans = factorial.factorial(0)
        self.assertEqual(1, stu_ans, ans.format(stu_ans))


if __name__ == '__main__':
    unittest.main()
