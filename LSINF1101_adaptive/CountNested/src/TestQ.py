#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


def list_generator():
    res = []
    for i in range(5, 10):
        res.append(multid_list_gen())
    return res

def multid_list_gen():
    res = []
    i = random.randint(1, 2)
    res.append([random.randint(1, 10) for _ in range(random.randint(1, 5))])
    if i <= 1: res[0].append(multid_list_gen())
    return res


class TestCount(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'count'), _("You did not name the method as expected."))

    def test_empty(self):
        a = []
        ans = _("Le compte pour une liste vide doit toujours être 0 et vous avez renvoyé {}.")
        stu_ans = q.count(2, a)
        corr_ans = 0
        self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans))

    def test_no_element(self):
        a = [1, 2, [3, 4], 5, 6, [7, 8]]
        ans = _("Le compte pour une liste sans n devrait être 0 et vous avez renvoyé {}.")
        stu_ans = q.count(9, a)
        corr_ans = 0
        self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans))

    def test_sure(self):
        a = [1, 2, [3, 4], 3, 6, [3, 8]]
        ans = _("Le compte pour une liste ayant n 3 fois devrait être 3 et vous avez renvoyé {}.")
        stu_ans = q.count(3, a)
        corr_ans = 3
        self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans))

    def test_flatten(self):
        lists = [list_generator() for i in range(5)]
        ans = _("Le compte pour la liste {} avec {} devrait être {} et vous avez renvoyé {}.")
        for l in lists:
            n = random.randint(1, 10)
            stu_ans = q.count(n, l)
            corr_ans = corr.count(n, l)
            self.assertEqual(corr_ans, stu_ans, ans.format(l, n, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
