#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrInterval as corr
import interval


class TestInterval(unittest.TestCase):
    def test_interval(self):
        a = [random.randint(1, 100) for _ in range(5)]
        b = a + [random.randint(1, 100) for _ in range(5)]
        c = [random.randint(1, 100) for _ in range(5)]
        ans = _("The belonging of {} to [{}, {}] is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = interval.interval(a[i], b[i], c[i])
            corr_ans = corr.interval(a[i], b[i], c[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(c[i], a[i], b[i], corr_ans, stu_ans))

    def test_bounds(self):
        a = [random.randint(1, 100) for _ in range(5)]
        ans = _("The belonging of {} to [{}, {}] is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = interval.interval(a[i], a[i], a[i])
            corr_ans = corr.interval(a[i], a[i], a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], a[i], a[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
