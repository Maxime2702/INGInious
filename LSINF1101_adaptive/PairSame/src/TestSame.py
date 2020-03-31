#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrSame as corr
import same


class TestFlag(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(same.Pair, '__eq__'), _("You did not provide the asked method."))

    def test_true(self):
        ans = _("The 2 objects are the same and your method returned {}.")
        stu_ans = same.Pair(9, 42)
        tmp = same.Pair(9, 42)
        self.assertTrue(stu_ans == tmp, ans.format(stu_ans == tmp))

    def test_false(self):
        ans = _("The 2 objects are not the same and your method returned {}.")
        stu_ans = same.Pair(6, 47)
        tmp = same.Pair(42, 9)
        self.assertFalse(stu_ans == tmp, ans.format(stu_ans == tmp))

    def test_none(self):
        ans = _("When None is given as parameter, you returned {}.")
        stu_ans = same.Pair(9, 42)
        self.assertFalse(stu_ans.__eq__(None), ans.format(stu_ans.__eq__(None)))


if __name__ == '__main__':
    unittest.main()
