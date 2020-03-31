#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrQ as corr
import q


def generate_intel(file, width, over_width=False):
    text = ''
    with open(file, 'w+') as f:
        for _ in range(random.randint(6, 10)):
            line =  ''.join([random.choice(string.ascii_letters) for _ in range(random.randint(width-3, width))]) + '\n'
            f.write(line)
            text += line
        if over_width: 
            line = ''.join([random.choice(string.ascii_letters) for _ in range(random.randint(width, width+6))]) + '\n'
            f.write(line)
            text += line
    return text


class TestTable(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'table'), _("You did not name the method as expected."))

    def test_normal_use(self):
        width = random.randint(4, 12)
        filename = 'data.txt'
        text = generate_intel(filename, width)
        ans = "Avec le texte: {}\nVotre fichier contenait: {}"
        q.table(filename, 'test.txt', width)
        corr.table(filename, 'corr.txt', width)
        with open('test.txt', 'r') as f, open('corr.txt', 'r') as fc:
            stu_ans = f.read()
            corr_ans = fc.read()
        if corr_ans + '\n' == stu_ans:
            self.fail('Votre programme ajoute une ligne vide à la fin des fichiers.')
        self.assertEqual(corr_ans, stu_ans, ans.format(text, stu_ans))

    def test_over_width(self):
        width = random.randint(4, 12)
        filename = 'data.txt'
        text = generate_intel(filename, width, True)
        ans = "Vous ne traitez pas les cas de mots trop grands!\nAvec le texte: {}\nVotre fichier contenait: {}"
        q.table(filename, 'test.txt', width)
        corr.table(filename, 'corr.txt', width)
        with open('test.txt', 'r') as f, open('corr.txt', 'r') as fc:
            stu_ans = f.read()
            corr_ans = fc.read()
        if corr_ans + '\n' == stu_ans:
            self.fail('Votre programme ajoute une ligne vide à la fin des fichiers.')
        self.assertEqual(corr_ans, stu_ans, ans.format(text, stu_ans))


if __name__ == '__main__':
    unittest.main()
