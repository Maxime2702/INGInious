#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrGcd as corr
import gcd


class TestGcd(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(gcd, 'gcd'), _("You did not name the method as expected."))

    def test_zero(self):
        a = 0
        b = random.randint(1, 100)
        ans = _("Test zero - The greatest common divisor between {} and {} is {} and you returned {}.")
        stu_ans = gcd.gcd(a, b)
        corr_ans = corr.gcd(a, b)
        self.assertEqual(corr_ans, stu_ans, ans.format(a, b, corr_ans, stu_ans))

    def test_gcd(self):
        a = [random.randint(1, 100) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        ans = _("The greatest common divisor between {} and {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = gcd.gcd(a[i], b[i])
            corr_ans = corr.gcd(a[i], b[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], b[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
