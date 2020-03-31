#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrSum as corr
import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        i = random.randint(1, 100) 
        ans = _("La somme des {} premiers entiers est {} et tu as renvoyé {}.")
        stu_ans = sum.sum(i)
        corr_ans = corr.sum(i)
        self.assertEqual(corr_ans, stu_ans, ans.format(i, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
