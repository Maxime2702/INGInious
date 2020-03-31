#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrAverage as corr
import average


class TestAverage(unittest.TestCase):
    def test_average(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The average of {} is {} and you returned {}.")
        for i in range(len(lists)):
            stu_ans = average.average(lists[i])
            corr_ans = corr.average(lists[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(lists[i], corr_ans, stu_ans))

    def test_empty(self):
        lst = []
        ans = _("When the list is empty you should return None.")
        self.assertEqual(None, average.average(lst), ans)


if __name__ == '__main__':
    unittest.main()
