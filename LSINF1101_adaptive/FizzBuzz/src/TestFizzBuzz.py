#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFizzBuzz as corr
import fizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        a = [random.randint(1, 100) for _ in range(5)]
        ans = _("With {} as input the program should return {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = fizzBuzz.fizz_buzz(a[i])
            corr_ans = corr.fizz_buzz(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_sure_case(self):
        a = [5, 15, 30, 45, 27]
        ans = _("With {} as input the program should return {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = fizzBuzz.fizz_buzz(a[i])
            corr_ans = corr.fizz_buzz(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
