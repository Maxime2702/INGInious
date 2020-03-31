#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest

import Corr as corr
import template0 as t0
import template1 as t1
import template2 as t2
import template3 as t3


class TestPrimes(unittest.TestCase):
    def test_working(self):
        ans = _("Votre test renvoit {} alors que le code fonctionne.")
        stu_ans = t0.test()
        self.assertTrue(stu_ans, ans.format(stu_ans))

    def test_min_index(self):
        ans = _("Votre test renvoit {} alors que le code renvoit l'index de la valeur min et non max.")
        stu_ans = t1.test()
        self.assertFalse(stu_ans, ans.format(stu_ans))


    def test_max(self):
        ans = _("Votre test renvoit {} alors que le code renvoit la valeur max et non son index.")
        stu_ans = t2.test()
        self.assertFalse(stu_ans, ans.format(stu_ans))


    def test_none(self):
        ans = _("Votre test renvoit {} alors que le code ne traite pas les listes vides.")
        stu_ans = t3.test()
        self.assertFalse(stu_ans, ans.format(stu_ans))


if __name__ == '__main__':
    unittest.main()
