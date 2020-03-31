#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQBF as corr
import qbf


CORRECT = ("2.0\n4.5\n1.2", 4.5, "Votre fonction ne renvoit pas le maximum dans un fichier de lignes adéquates.")
MULTI = ("8.0 7.0 10.0\n5.0\n12.0 14.0", 5.0, "Avec un fichier comprenant des lignes avec plusieurs nombre, vous ne renvoyez pas le maximum des lignes adéquates.")
MULTI_NS = ("8.0 7.0 10.0\n12.0 14.0", -1, "Avec un fichier sans lignes adéquates vous ne renvoyez pas -1")
NADEQUATE = ("hello\n1.0\n5.0\ntest", 5.0, "Gérez-vous convenablement les lignes non-adéquates?")
NADEQUATE_NS = ("hello\ntest", -1, "Avec un fichier sans lignes adéquates vous ne renvoyez pas -1")
NEGATIVE = ("-3.0\n-7.0", -1, "Gérez-vous convenablement les nombres négatifs?")

TESTS = [CORRECT, MULTI, MULTI_NS, NADEQUATE, NADEQUATE_NS, NEGATIVE]


class TestQBF(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(qbf, 'get_max'), _("Vous n'avez pas fourni la méthode get_max."))

    def test_cases(self):
        for t in TESTS:
            with open('test.txt', 'w') as f:
                f.write(t[0])
            ans = t[2]
            stu_ans = qbf.get_max('test.txt')
            corr_ans = t[1]
            self.assertEqual(corr_ans, stu_ans, ans)

    def test_IOError(self):
        ans = 'Traitez-vous correctement les fichiers manquants?'
        stu_ans = qbf.get_max('IOError.txt')
        corr_ans = -1
        self.assertEqual(corr_ans, stu_ans, ans)



if __name__ == '__main__':
    unittest.main()
