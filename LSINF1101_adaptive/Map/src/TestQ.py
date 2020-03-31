#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from copy import deepcopy

import CorrQ as corr
import q

def square(e):
    return e*e

def reverse(e):
    return -e

class TestMap(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'map'), _("You did not name the method as expected."))

    def test_basic_case(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        ans = _("L'utilisation de votre fonction avec une liste et une fonction square a renvoyé un résultat inattendu.")
        corr_l = deepcopy(a)
        stu_ans = q.map(square, a)
        if a != corr_l:
            self.fail("Il ne vous était pas demandé d'altérer la liste fournie.")
        corr_ans = corr.map(square, corr_l)
        self.assertEqual(corr_ans, stu_ans, ans)

    def test_other_function(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        ans = _("Votre fonction ne semble pas tolérer le passage d'autre fonctions en paramètres.")
        corr_l = deepcopy(a)
        stu_ans = q.map(reverse, a)
        if a != corr_l:
            self.fail("Il ne vous était pas demandé d'altérer la liste fournie.")
        corr_ans = corr.map(reverse, corr_l)
        self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
