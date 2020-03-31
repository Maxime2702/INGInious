#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrQ as corr
import q


FUN_NAMES = ['square', 'add2', 'mul3']

class TestLambda(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'asked_fun'), _("You did not name the method as expected."))

    def test_lambda(self):
        for n in FUN_NAMES:
            stud_ans = q.asked_fun(n)
            self.assertEqual(stud_ans.__name__, '<lambda>', "Utilisez lambda et pas des fonctions.")
    
    def test_rand(self):
        ans = _("Votre fonction {} renvoyée par votre fonction ``asked_fun`` renvoit {} avec ``x == {}`` au lieu de {}.")
        for n in FUN_NAMES:
            x = random.randint(10, 100)
            stud_ans = q.asked_fun(n)(x)
            corr_ans = corr.asked_fun(n)(x)
            self.assertEqual(corr_ans, stud_ans, ans.format(n, stud_ans, x, corr_ans))

