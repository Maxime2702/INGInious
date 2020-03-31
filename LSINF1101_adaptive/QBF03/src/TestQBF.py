#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQBF as corr
import qbf


class TestQBF(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(qbf, 'chiffres_pairs'), ("Vous n'avez pas fourni la méthode demandée."))

    def test_chiffres_pairs(self):
        seed = [1, 10, 100, 1000, 10000, 22, 0]
        ans = {True: 'pair', False: 'impair'}
        def fb(res): 
            return _("Le nombre de chiffre de {} est un nombre " + ans[res] + " et vous avez renvoyé {}")
        for i in seed:
            stu_ans = qbf.chiffres_pairs(i)
            corr_ans = corr.chiffres_pairs(i)
            self.assertEqual(corr_ans, stu_ans, fb(corr_ans).format(i, stu_ans))


if __name__ == '__main__':
    unittest.main()
