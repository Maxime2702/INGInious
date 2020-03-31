#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import CorrQ as corr
import q


def reverse(x):
    return -x

def sqrt(x):
    return math.sqrt(x)
    


class TestCompose(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'compose'), _("You did not name the method as expected."))

    def test_basic_case(self):
        ans = _("L'utilisation de votre fonction compose ne fournit pas la fonction demandée.")
        try:
            stu_func = q.compose(reverse, sqrt)
            if not callable(stu_func):
                self.fail("Renvoyez-vous réellement une fonction appelable?")
            stu_ans = stu_func(4)
            corr_ans = -2
            self.assertEqual(corr_ans, stu_ans, ans)
        except ValueError:
            self.fail("Composez-vous bien les fonctions dans l'ordre? Pour compose(f, g) -> f(g(x))")
        except TypeError:
            self.fail("Renvoyez-vous réellement une fonction appelable?")


if __name__ == '__main__':
    unittest.main()
