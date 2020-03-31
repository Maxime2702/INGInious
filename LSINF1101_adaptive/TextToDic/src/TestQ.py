#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


TEXTS = [('ceci est un test', {'ceci': 1, 'est': 1, 'un': 1, 'test': 1}, "Vous ne créez pas un dictionnaire reflétant le contenu du fichier."), ('ceci ceci est', {'ceci': 2, 'est': 1}, "Vous avez un problème apparaissant plus qu'une fois"), ('', {}, "Pour un texte vide, le dictionaire devrait rester vide.")]

DIC = {'Aristote': 1, 'Pomme':2, 'Code': 2}

class TestFileReading(unittest.TestCase):
    def test_exist_memo(self):
        self.assertTrue(hasattr(q, 'occ') and hasattr(q, 'create_dictionary'), _("You did not name the method as expected."))

    def test_dic(self):
        for t in TEXTS:
            with open('test.txt', 'w') as f:
                f.write(t[0])
            stu_ans = q.create_dictionary('test.txt')
            corr_ans = t[1]
            self.assertEqual(corr_ans, stu_ans, t[2])

    def test_occ(self):
        for w in DIC.keys():
            stu_ans = q.occ(DIC, w)
            corr_ans = DIC[w]
            self.assertEqual(corr_ans, stu_ans, 'Pour le dictionaire donné, votre code ne renvoit pas la bonne occurence des mots.')

    def test_occ_oov(self):
        stu_ans = q.occ(DIC, 'Francou')
        self.assertEqual(0, stu_ans, 'Pour un mot non présent dans le dictionaire, occ ne renvoit pas 0.')
        


if __name__ == '__main__':
    unittest.main()
