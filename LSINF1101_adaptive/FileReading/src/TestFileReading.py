#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFileReading as corr
import filereading


s = "Ceci est un test\nTu connais les yoyos?\nVous aviez déjà tous des console mais jouer avec des batons c'était cool."
files = ['0.txt', '1.txt']
texts = {'0.txt': s.split('\n')[0], '1.txt': s}
with open(files[0], 'w+') as f:
    f.write(s.split('\n')[0])
with open(files[1], 'w+') as f:
    f.write(s)

class TestFileReading(unittest.TestCase):
    def test_exist_memo(self):
        self.assertTrue(hasattr(filereading, 'line_count'), "@1@: " + _("You did not name the method as expected."))

    def test_exist_fibo(self):
        self.assertTrue(hasattr(filereading, 'char_count'), "@2@: " + _("You did not name the method as expected."))


    def test_exist_fact(self):
        self.assertTrue(hasattr(filereading, 'space'), "@4@: " + _("You did not name the method as expected."))

    def test_exist_fact(self):
        self.assertTrue(hasattr(filereading, 'capitalize'), "@5@: " + _("You did not name the method as expected."))

    def test_line_count(self):
        ans = "@1@: " + ("Le nombre de lignes du fichier avec le contenu:\n {}\nEst {} et vous avez renvoyé {}.")
        for f in files:
            stu_ans = filereading.line_count(f)
            corr_ans = len(texts[f].split('\n'))
            self.assertEqual(corr_ans, stu_ans, ans.format(texts[f], corr_ans, stu_ans))

    def test_char_count(self):
        ans = "@2@: " + ("Le nombre de caractères du fichier avec le contenu:\n {}\nEst {} et vous avez renvoyé {}.")
        for f in files:
            stu_ans = filereading.char_count(f)
            corr_ans = len(texts[f])
            self.assertEqual(corr_ans, stu_ans, ans.format(texts[f], corr_ans, stu_ans))

    def test_space(self):
        ans = "@4@: " + ("Ce que vous écrivez dans le fichier:\n{}\nNe correspond pas à ce qui est aux {}(n) espaces attendus.")
        n = random.randint(2, 4)
        filereading.space('test.txt', n)
        with open('test.txt', 'r') as f:
            stu_ans = f.read()
            self.assertEqual(" " * n, stu_ans, ans.format(stu_ans, n))

    def test_capitalize(self):
        ans = "@5@: " + ("Le fichier avec le contenu:\n {}\nEst altéré et envoyé dans un autre fichier avec un format non attendu: {}")
        for f in files:
            filereading.capitalize(f, 'test.txt')
            corr_ans = texts[f].upper()
            with open('test.txt', 'r') as sf:
                stu_ans = sf.read()
                self.assertEqual(corr_ans, stu_ans, ans.format(texts[f], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
