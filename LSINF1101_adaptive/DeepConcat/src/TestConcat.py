#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import string

import CorrConcat as corr
import concat


def list_generator():
    res = []
    for i in range(5, 10):
        res.append(multid_list_gen())
    return res

def multid_list_gen():
    res = []
    i = random.randint(1, 2)
    res.append([random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 5))])
    if i <= 1: res[0].append(multid_list_gen())
    return res


class TestFlatten(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(concat, 'deep_concat'), _("You did not name the method as expected."))

    def test_empty(self):
        a = []
        ans = _("The flatten version of {} is supposed to be an empty string and you returned {}. \n You should watch you behaviour in case of empty lists.")
        for i in range(len(a)):
            stu_ans = concat.deep_concat(a)
            corr_ans = corr.deep_concat(a)
            self.assertEqual(corr_ans, stu_ans, ans.format(a, stu_ans))

    def test_deep_concat(self):
        lists = [list_generator() for i in range(5)]
        ans = _("The flatten version of {} is {} and you returned {}.")
        for i in range(len(lists)):
            stu_ans = concat.deep_concat(lists[i])
            corr_ans = corr.deep_concat(lists[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(lists[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
