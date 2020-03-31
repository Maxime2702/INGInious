#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFlatten as corr
import flatten


def list_generator():
    res = []
    for i in range(5, 10):
        res.append(multid_list_gen())
    return res

def multid_list_gen():
    res = []
    i = random.randint(1, 2)
    res.append([random.randint(1, 100) for _ in range(random.randint(1, 5))])
    if i <= 1: res[0].append(multid_list_gen())
    return res


class TestFlatten(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(flatten, 'flatten'), _("You did not name the method as expected."))

    def test_empty(self):
        a = []
        ans = _("The flatten version of {} is {} and you returned {}. \n You should watch you behaviour in case of empty lists.")
        for i in range(len(a)):
            stu_ans = flatten.flatten(a)
            corr_ans = corr.flatten(a)
            self.assertEqual(corr_ans, stu_ans, ans.format(a, corr_ans, stu_ans))

    def test_flatten(self):
        lists = [list_generator() for i in range(5)]
        ans = _("The flatten version of {} is {} and you returned {}.")
        for i in range(len(lists)):
            stu_ans = flatten.flatten(lists[i])
            corr_ans = corr.flatten(lists[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(lists[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
