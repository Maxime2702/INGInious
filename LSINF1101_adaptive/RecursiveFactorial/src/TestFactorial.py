#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFactorial as corr
import factorial


class Counter(object):
    def __init__(self, fun):
        self._fun = fun
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self._fun(*args, **kwargs)


class TestFactorial(unittest.TestCase):
    def setUp(self):
        a = random.randint(6, 69)
        ans = _("You did not use recursion in your algorithm ")
        factorial.factorial = Counter(factorial.factorial)
        stu_ans = factorial.factorial(a)
        self.assertNotEqual(1, factorial.factorial.counter, ans)

    def test_factorial(self):
        a = [random.randint(1, 69) for _ in range(5)]
        ans = _("The factorial of the integer {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = factorial.factorial(a[i])
            corr_ans = corr.factorial(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_zero(self):
        ans = _("The factorial of 0 is 1 and you returned {}.")
        stu_ans = factorial.factorial(0)
        self.assertEqual(1, stu_ans, ans.format(stu_ans))

    def test_negatives(self):
        a = [-(random.randint(1, 100)) for _ in range(5)]
        ans = _("The factorial of a negative integer {} should be None and you returned {}.")
        for i in range(len(a)):
            stu_ans = factorial.factorial(a[i])
            self.assertEqual(None, stu_ans, ans.format(a[i], stu_ans))


if __name__ == '__main__':
    unittest.main()
