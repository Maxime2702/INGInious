#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrMedian as corr
import median


class TestMedian(unittest.TestCase):
    def test_median(self):
        a = [random.randint(1, 100) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        c = [random.randint(1, 100) for _ in range(5)]
        ans = _("The median of {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = median.median(a[i], b[i], c[i])
            corr_ans = corr.median(a[i], b[i], c[i])
            self.assertEqual(corr_ans, stu_ans, ans.format([a[i], b[i], c[i]], corr_ans, stu_ans))

    def test_specific_median(self):
        a = random.randint(1, 100)
        b = a + 1
        c = a - 1
        ans = _("The median of {} is {} and you returned {}.")
        stu_ans = median.median(a, b, c)
        corr_ans = corr.median(a, b, c)
        self.assertEqual(corr_ans, stu_ans, ans.format([a, b, c], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
