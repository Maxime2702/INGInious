#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrM07 as corr
import search


BASIC = ("ceci est un test", ['ceci', 'est', 'un', 'test'], "Votre programme ne parvient pas à extraire les mots d'une phrase") 
LOWER = ("Ceci Est Un Test", ['ceci', 'est', 'un', 'test'], "Mettez-vous bien les mots en minuscule?") 
PUNCTUATION = ("ceci . est , un test ?", ['ceci', 'est', 'un', 'test'], "Supprimez-vous bien la ponctuation?")
DELETION = ("they've ceci est ?un 'test", ['theyve', 'ceci', 'est', 'un', 'test'], "La ponctuation doit être supprimée et non remplacée par un espace.")  
WORDS = [BASIC, LOWER,  PUNCTUATION, DELETION]

BASE = (['the', 'of'], [0, 1], "Vous ne trouvez pas les lignes de deux mots apparaissants dans les mêmes lignes.")
CONFLICT = (['while', 'jedi'], [], "Vous ne traitez pas correctement les mots n'ayant pas de lignes communes.")
OOV = (['arayraygra'], [], "Vous ne traitez pas correctement les mots non présents dans l'index (vous devez renvoyez une liste vide).")
LOOKED_WORDS = [BASE, CONFLICT, OOV]


class TestM07(unittest.TestCase):  
    def test_IOError(self):
        try:
            search.readfile('IOError.txt') 
        except IOError: 
            self.fail("Vous ne traitez pas les fichiers vides")

    def test_read(self):
        txt = 'ceci est un test\nVas tu réussir ?'
        with open('test.txt', 'w') as f:
            f.write(txt)
        stu_ans = search.readfile('test.txt')
        if '\n' in stu_ans[0]:
            self.fail("Votre fonction ne renvoit pas que les phrases mais également les retours de ligne.")
        self.assertEqual(txt.split('\n'), stu_ans, "Votre fonction readfile ne renvoit pas le tableau attendu pour un fichier texte.")

    def test_get_words(self):
        for line in WORDS:
            stu_ans = search.get_words(line[0])
            self.assertEqual(line[1], stu_ans, line[2])

    def test_create_index(self):
        txt = "While the Congress of the Republic endlessly debates\nthis alarming chain of events, the Supreme Chancellor has\nsecretly dispatched two Jedi Knights."
        with open('test.txt', 'w') as f:
             f.write(txt)
        corr_ans = corr.create_index('test.txt')
        stu_ans = search.create_index('test.txt')
        self.assertEqual(corr_ans, stu_ans, "L'index que vous renvoyez ne correspond pas à celui attendu.")

    def test_get_lines(self):
        txt = "While the Congress of the Republic endlessly debates\nthis alarming chain of events, the Supreme Chancellor has\nsecretly dispatched two Jedi Knights."
        with open('test.txt', 'w') as f:
             f.write(txt)
        index = corr.create_index('test.txt')
        for test in LOOKED_WORDS:
            stu_ans = search.get_lines(test[0], index)
            self.assertEqual(test[1], stu_ans, test[2])
 

if __name__ == '__main__':
    unittest.main()

