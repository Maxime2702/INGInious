#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrRecherche as corr
import recherche as stu


class TestRecherche(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(True, "recherche" in dir(stu), _("You did not name the method as expected."))
    
    def test_recherche(self):
        length = random.randint(1, 20)
        m = [[random.randint(0, 100) for _ in range(length)] for _ in range(random.randint(1, 20))]
        ans = _("\nFor m = {} and v = {}, the expected recherche is: \n {} but you returned: \n{}.")
        for v in range(100):
            stu_ans = stu.recherche(m,v)
            corr_ans = corr.recherche(m,v)
            self.assertEqual(corr_ans, stu_ans, ans.format(m, v, corr_ans, stu_ans))

    def test_small_mat(self):
        m = [[42]]
        v = 41
        ans = _("\nFor m = {} and v = {}, the expected recherche is: \n {} but you returned: \n{}.")
        stu_ans = stu.recherche(m,v)
        corr_ans = False
        self.assertEqual(corr_ans, stu_ans, ans.format(m, 41, corr_ans, stu_ans))

        v = 42
        stu_ans = stu.recherche(m,v)
        corr_ans = True
        self.assertEqual(True, stu_ans, ans.format(m, 42, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
