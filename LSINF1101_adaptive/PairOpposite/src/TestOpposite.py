#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrOpposite as corr
import opposite


class TestOpposite(unittest.TestCase):
    def test_opposite(self):
        a = [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(random.randint(1, 20))]
        ans = _("The opposite of {} is {} and you returned {}")
        for e in a:
            stu_ans = opposite.Pair(e[0], e[1]).opposite()
            if not isinstance(stu_ans, opposite.Pair):
                self.fail("Vous ne renvoyez pas une instance de la classe Pair")
            self.assertEqual(corr.Pair(-e[0], -e[1]), stu_ans, ans.format(e, str(-e[0])+', '+str(-e[1]), stu_ans))

    def test_0(self):
        ans = _("The opposite of 0,0 is 0,0 and you returned {}")
        stu_ans = opposite.Pair(0, 0).opposite()
        if not isinstance(stu_ans, opposite.Pair):
            self.fail("Vous ne renvoyez pas une instance de la classe Pair")
        self.assertEqual(corr.Pair(0, 0), stu_ans, ans.format(stu_ans))


if __name__ == '__main__':
    unittest.main()
