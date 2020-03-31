#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrMax as corr
import max


class TestMax(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(True, hasattr(max, 'maximum_index'), _("You did not name the method as expected."))

    def test_max(self):
        lists = [[random.randint(-100, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The index of the maximum of {} is {} and you returned {}.")
        for i in range(len(lists)):
            stu_ans = max.maximum_index(lists[i])
            corr_ans = corr.maximum(lists[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(lists[i], corr_ans, stu_ans))

    def test_empty(self):
        lst = []
        ans = _("When the list is empty you should return None.")
        self.assertEqual(None, max.maximum_index(lst), ans)


if __name__ == '__main__':
    unittest.main()
