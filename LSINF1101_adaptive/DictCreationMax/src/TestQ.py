#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

CORRECT = ([(1, 2), (2, 3), (3, 4)], {1: 2, 2: 3, 3: 4}, "Votre programme ne semble pas faire la transformation demandée.")
CORRECT_W_MULTI = ([(1, 2), (2, 3), (3, 2), (3, 4), (3, 3)], {1: 2, 2: 3, 3: 4},"Votre programme ne semble pas faire la transformation demandée quand il y a plusieurs éléments pour un même X. Stocke-t-il bien le maximum?")
EMPTY = ([], {}, "Votre programme ne semble pas produire un dictionnaire vide pour une liste vide.")

TESTS = [CORRECT, CORRECT_W_MULTI, EMPTY]


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'create_dict_max'), _("You did not name the method as expected."))

    def test_cases(self):
        for t in TESTS:
            ans = t[2]
            corr_ans = t[1]
            stu_ans = q.create_dict_max(t[0])
            self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
