#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestCount(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'count'), _("You did not name the method as expected."))

    def test_count(self):
        l = [[(random.randint(0, 3), random.randint(0, 3)) for _ in range(5)] for _ in range(5)]
        ans = _("Le comtpe que vous renvoyez pour l'événement {} avec {} comme input est {} et devrait être {}.")
        for e in l:
            i, j = e[0]
            stu_ans = q.count(e, i, j)
            corr_ans = corr.count(e, i, j)
            self.assertEqual(corr_ans, stu_ans, ans.format((i, j), e, stu_ans, corr_ans))

    def test_in(self):
        l = [(1, 1), (2, 1), (1, 1)]
        ans = _("Le comtpe que vous renvoyez pour l'événement {} avec {} comme input est {} et devrait être {}.")
        i, j = 1, 1
        stu_ans = q.count(l, i, j)
        self.assertEqual(2, stu_ans, ans.format((i, j), l, stu_ans, 2))

    def test_not_in(self):
        l = [(1, 1), (2, 1), (1, 1)]
        ans = _("Le comtpe que vous renvoyez pour l'événement {} avec {} comme input est {} et devrait être {}.")
        i, j = 0, 0
        stu_ans = q.count(l, i, j)
        self.assertEqual(0, stu_ans, ans.format((i, j), l, stu_ans, 0))


if __name__ == '__main__':
    unittest.main()
