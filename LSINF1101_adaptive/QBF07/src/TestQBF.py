#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQBF as corr
import qbf


WORDS_BASE = ["while", "the", "congress", "of", "the", "republic", "endlessly", "debates", "this", "alarming", "chain", "of", "events", "the", "supreme", "chancellor", "has", "secretly", "dispatched", "two", "jedi", "knights"]
WORDS_NE = ["while", "the"]
WORDS_SAME_OCC = ['while', 'while', 'while', 'the', 'the', 'a', 'a', 'same', 'old']

CORRECT = (WORDS_BASE, 2, [(3,"the"), (2,"of")], "Votre fonction ne renvoit pas les 2 éléments les plus fréquents.")
NE = (WORDS_NE, 3, [(1,"the"), (1,"while")], "Votre fonction ne réagit pas bien à un n plus grand que le nombre de mots.")
SAME_OCC = (WORDS_SAME_OCC, 2, [(3,"while"), (2,"the"), (2, 'a')], "Votre fonction ne traite pas correctement les cas où plusieurs mots ont la même occurrence.")

TESTS = [CORRECT, NE, SAME_OCC]


class TestQBF(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(qbf, 'topk_words'), _("Vous n'avez pas fourni la méthode topk_words."))

    def test_cases(self):
        for t in TESTS:
            ans = t[3]
            stu_ans = sorted(qbf.topk_words(t[0], t[1]))
            corr_ans = sorted(t[2])
            self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
