#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrGd as corr
import gd


class TestGd(unittest.TestCase):
    def test_gd(self):
        a = [random.randint(1, 100) for _ in range(5)]
        ans = _("The greatest divisor of {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = gd.gd(a[i])
            corr_ans = corr.gd(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_zero(self):
        ans = _("The expected answer for the greatest divisor of 0 should be None and you returned {}.")
        stu_ans = gd.gd(0)
        self.assertEqual(None, stu_ans, ans.format(stu_ans))

    def test_one(self):
        ans = _("The expected answer for the greatest divisor of 0 should be None and you returned {}.")
        stu_ans = gd.gd(1)
        self.assertEqual(None, stu_ans, ans.format(stu_ans))


if __name__ == '__main__':
    unittest.main()
