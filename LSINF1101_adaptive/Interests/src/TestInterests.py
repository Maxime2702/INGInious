#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrInterests as corr
import interests


class TestInterests(unittest.TestCase):
    def test_interests(self):
        a = [random.randint(1, 10000) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        c = [random.randint(1, 20) for _ in range(5)]
        ans = _("When calling interests(base, y, x) with base = {}€ , y = {}% and x = {} years you returned {} but the expected value was {}.")
        for i in range(len(a)):
            stu_ans = interests.interests(a[i], b[i], c[i])
            corr_ans = corr.interests(a[i], b[i], c[i])
            self.assertAlmostEqual(corr_ans, stu_ans, places = 0, msg = ans.format(a[i], b[i], c[i], stu_ans, corr_ans))


if __name__ == '__main__':
    unittest.main()
