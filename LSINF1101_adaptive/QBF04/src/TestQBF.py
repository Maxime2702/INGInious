#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQBF as corr
import qbf


class TestQBF(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(qbf, 'positions'), ("Vous n'avez pas fourni la fonction demandée."))

    def test_empty(self):
        ans = _("Le pattern n'apparait pas dans la chaîne proposée et vous avez renvoyé {}.")
        stu_ans = qbf.positions('ab', 'GDECF')
        self.assertEqual([], stu_ans, ans.format(stu_ans))

    def test_joker(self):
        ans = _("Les patterns avec jokers ne semblent pas fonctionner. Vous avez renvoyé {} à la place de {}.")
        inputs = (("?B","CAbbF"), ("C?","CAbcEF"), ("??","CAAAB"))
        for e in inputs:
            stu_ans = qbf.positions(e[0], e[1])
            corr_ans = corr.positions(e[0], e[1])
            self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))

    def test_simplest(self):
        ans = _("Les patterns ne semblent pas être reconnus. Vous avez renvoyé {} à la place de {}.")
        inputs = (("bB","CbbbF"), ("Ca","CAbcEF"), ("ab","CAAAB"))
        for e in inputs:
            stu_ans = qbf.positions(e[0], e[1])
            corr_ans = corr.positions(e[0], e[1])
            self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))




if __name__ == '__main__':
    unittest.main()
