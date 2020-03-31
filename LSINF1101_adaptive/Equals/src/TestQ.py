#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

CORRECT = ([[1, 2], [3, 4]], {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}, True, "Votre programme ne semble pas traiter l'égalité simple des structures.")
CORRECT_W_0 = ([[0, 2], [3, 4]], {(0, 1): 2, (1, 0): 3, (1, 1): 4}, True, "Votre programme ne semble pas traiter l'égalité quand il y a un 0 dans la lsite et donc rien dans le dictionnaire.")
CORRECT_W_E = ([[1, 2], [3, 4]], {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4, (2, 0): 5}, True, "Votre programme ne semble pas traiter le fait que le dictionnaire puisse posséder plus d'éléments que juste la liste.")
INCOMPLETE = ([[1, 2], [3, 4]], {(0, 0): 1, (0, 1): 2, (1, 0): 3}, False, "Votre programme semble ne pas détecter d'inégalité, ici une entrée manquante dans le dictionnaire.")
WRONG_KEYS = ([[1, 2], [3, 4]], {(0, 3): 1, (0, 1): 2, (1, 0): 3}, False, "VOtre programme teste seulement les valeurs et pas les clés comme emplacements.")
EMPTY = ([[0, 0], [0, 0]], {}, True, "Votre programme ne semble pas accepter un dictionnaire vide pour une liste remplie de 0.")


TESTS = [CORRECT, CORRECT_W_0, CORRECT_W_E, INCOMPLETE, WRONG_KEYS, EMPTY]


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'equal'), _("You did not name the method as expected."))

    def test_cases(self):
        for t in TESTS:
            ans = t[3]
            corr_ans = t[2]
            stu_ans = q.equal(t[0], t[1])
            self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
