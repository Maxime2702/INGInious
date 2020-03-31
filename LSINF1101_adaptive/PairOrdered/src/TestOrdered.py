#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrOrdered as corr
import ordered


class TestOrdered(unittest.TestCase):
    def test_exist(self):
        self.assertTrue((hasattr(ordered.OrderedPair, 'set_a') and hasattr(ordered.OrderedPair, 'set_b')),
                        _("You did not provide the asked methods."))

    def test_set_a(self):
        a = [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(random.randint(1, 20))]
        a.append((1, 0))
        ans = _("The pair {} is {} and you labelled it as {}ly ordered.")
        for e in a:
            stu_ans = ordered.OrderedPair()
            if stu_ans.set_b(e[0]) is not None or stu_ans.set_a(e[1]) is not None:
                self.fail("Vos fonctions sont censées ne rien renvoyer.")
            corr_ans = corr.OrderedPair()
            corr_ans.set_b(e[0]), corr_ans.set_a(e[1])
            self.assertEqual(corr_ans.ordered, stu_ans.ordered, ans.format(e, corr_ans.ordered, stu_ans.ordered))

    def test_set_b(self):
        a = [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(random.randint(1, 20))]
        a.append((1, 0))
        ans = _("The pair {} is {} and you labelled it as {}ly ordered.")
        for e in a:
            stu_ans = ordered.OrderedPair()
            if stu_ans.set_a(e[0]) is not None or stu_ans.set_b(e[1]) is not None:
                self.fail("Vos fonctions sont censées ne rien renvoyer.")
            corr_ans = corr.OrderedPair()
            corr_ans.set_a(e[0]), corr_ans.set_b(e[1])
            self.assertEqual(corr_ans.ordered, stu_ans.ordered, ans.format(e, corr_ans.ordered, stu_ans.ordered))

    def test_0(self):
        ans = _("The pair 0,0 is ordered and you returned {}")
        stu_ans = ordered.OrderedPair()
        stu_ans.set_a(1), stu_ans.set_a(0)
        self.assertEqual(True, stu_ans.ordered, ans.format(stu_ans))


if __name__ == '__main__':
    unittest.main()
