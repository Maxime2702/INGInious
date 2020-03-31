#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import CorrQ as corr
import q


def square(x):
    return x**2

class TestCompose(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'fun_repetition'), _("You did not name the method as expected."))

    def test_basic_case(self):
        ans = _("L'utilisation de votre fun_repetition compose ne fournit pas la fonction demandée.")
        try:
            stu_func = q.fun_repetition(square, 2)
            if not callable(stu_func):
                self.fail("Renvoyez-vous réellement une fonction appelable?")
            stu_ans = stu_func(2)
            corr_ans = 16
            self.assertEqual(corr_ans, stu_ans, ans)
        except TypeError:
            self.fail("Renvoyez-vous réellement une fonction appelable?")


if __name__ == '__main__':
    unittest.main()
