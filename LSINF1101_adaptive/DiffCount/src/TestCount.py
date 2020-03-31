#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrCount as corr
import count


class TestCount(unittest.TestCase):
    def test_count(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The number of different elements of {} is {} and you returned {}.")
        for i in range(len(lists)):
            stu_ans = count.count(lists[i])
            corr_ans = corr.count(lists[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(lists[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
