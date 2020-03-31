#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import string

import CorrQBF as corr
import qbf


class TestQBF(unittest.TestCase):
    def test_exist(self):
        self.assertTrue((hasattr(qbf, 'CD') and hasattr(qbf.CD, '__init__') and hasattr(qbf.CD, '__str__')), "Vous n'avez pas fourni la calle CD ou les méthodes init ou str.")

    def test_str(self):
        author = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        title = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        duration = random.randint(100, 350) 
        ans = _("Avec les données: {}, {} et {}, vous avez créé le CD {} plutot que {}")
        stu_ans = qbf.CD(author, title, duration)
        corr_ans = corr.CD(author, title, duration)
        self.assertEqual(str(corr_ans), str(stu_ans), ans.format(author, title, duration, stu_ans, corr_ans))

    def test_multi(self):
        for i in range(3):
            author = ''.join(random.choice(string.ascii_letters) for _ in range(8))
            title = ''.join(random.choice(string.ascii_letters) for _ in range(8))
            duration = random.randint(100, 350) 
            ans = _("Avec les données: {}, {} et {}, vous avez créé le CD {} plutot que {}, mais incrémentez vous le numéro de série? Commence-t-il au bon numéro?")
            stu_ans = qbf.CD(author, title, duration)
            corr_ans = corr.CD(author, title, duration)
            self.assertEqual(str(corr_ans), str(stu_ans), ans.format(author, title, duration, stu_ans, corr_ans))


if __name__ == '__main__':
    unittest.main()
