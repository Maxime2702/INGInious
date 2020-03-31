#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestCount(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'counts'), _("You did not name the method as expected."))

    def test_count(self):
        l = [[(random.randint(0, 3), random.randint(0, 3)) for _ in range(5)] for _ in range(5)]
        ans = _("Les comtpes que vous renvoyez avec {} comme input est {} et devrait être {}.")
        for e in l:
            stu_ans = q.counts(e, 4, 4)
            corr_ans = corr.counts(e, 4, 4)
            self.assertEqual(corr_ans, stu_ans, ans.format(e, stu_ans, corr_ans))

if __name__ == '__main__':
    unittest.main()
