#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFactorial as corr
import factorial


class TestFactorial(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(factorial, 'fact'), _("You did not provide the requested method."))

    def test_factorial(self):
        a = [random.randint(1, 69) for _ in range(5)]
        ans = _("La factorielle de l'entier {} est {} et vous avez renvoyé {}.")
        for i in range(len(a)):
            stu_ans = factorial.fact(a[i])
            corr_ans = corr.factorial(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_zero(self):
        ans = _("La factorielle de 0 est 1 et vous avez renvoyé {}.")
        stu_ans = factorial.fact(0)
        self.assertEqual(1, stu_ans, ans.format(stu_ans))


if __name__ == '__main__':
    unittest.main()
