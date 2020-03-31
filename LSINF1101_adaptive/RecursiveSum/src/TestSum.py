#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from copy import deepcopy

import CorrSum as corr
import sum


class Counter(object):
    def __init__(self, fun):
        self._fun = fun
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self._fun(*args, **kwargs)


class TestFactorial(unittest.TestCase):
    def setUp(self):
        lst = [random.randint(1, 100) for _ in range(random.randint(4, 20))]
        ans = _("You did not use recursion in your algorithm ")
        sum.sum = Counter(sum.sum)
        stu_ans = sum.sum(lst)
        self.assertNotEqual(1, sum.sum.counter, ans)

    def test_sum(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sum of {} is {} and you returned {}.")
        for l in lists:
            corr_l = deepcopy(l)
            stu_ans = sum.sum(l)
            if l != corr_l:
                self.fail("Il ne vous était pas demandé d'altérer la liste fournie.")
            corr_ans = corr.sum(corr_l)
            self.assertEqual(corr_ans, stu_ans, ans.format(corr_l, corr_ans, stu_ans))

    def test_float(self):
        lists = [[random.random() for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sum of {} is {} and you returned {}. Do you handle floats?")
        for l in lists:
            corr_l = deepcopy(l)
            stu_ans = sum.sum(l)
            corr_ans = corr.sum(corr_l)
            self.assertAlmostEqual(corr_ans, stu_ans, 7, msg=ans.format(corr_l, corr_ans, stu_ans))

    def test_char(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sum list provided was {}. Did you take care of everything? ")
        for l in lists:
            l.append('e')
            try:
                corr_l = deepcopy(l)
                stu_ans = sum.sum(l)
                corr_ans = corr.sum(corr_l)
                self.assertEqual(corr_ans, stu_ans, ans.format(corr_l))
            except TypeError:
                self.assertFalse(True, ans.format(corr_l))

    def test_empty(self):
        lst = []
        ans = _("When the list is empty you should return 0.")
        self.assertEqual(0, sum.sum(lst), ans)


if __name__ == '__main__':
    unittest.main()
