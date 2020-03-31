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
        self.assertTrue(hasattr(q, 'recursive_min'), _("You did not name the method as expected."))

    def test_sure(self):
        a = list_generator()
        ans = _("Le min pour la liste {} est {} et vous avez renvoyé {}.")
        stu_ans = q.recursive_min(a)
        corr_ans = corr.recursive_min(a)
        self.assertEqual(corr_ans, stu_ans, ans.format(a, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
