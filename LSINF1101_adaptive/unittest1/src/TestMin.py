#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrMin as corr
import min


class TestMin(unittest.TestCase):
    def test_min(self):
        a = [random.randint(1, 100) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        c = [random.randint(1, 100) for _ in range(5)]
        ans = _("The minimum of {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = min.minimum(a[i], b[i], c[i])
            corr_ans = corr.minimum(a[i], b[i], c[i])
            self.assertEqual(corr_ans, stu_ans, ans.format([a[i], b[i], c[i]], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
