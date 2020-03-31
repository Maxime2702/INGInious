#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrSort as corr
import sortingHat


class TestSorter(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(sortingHat, 'house_designation'), _("You did not name the method as expected."))

    def test_multi_possible_houses(self):
        a = ['smart', 'wise', 'bold', 'brave', 'hard-working', 'loyal', 'wily', 'malignant']
        ans = _("Should you really belong to this house? \n Wasn't there any equals houses for the qualities {}?")
        corr_ans = corr.house_designation(a)
        for i in range(10):
            stu_ans = sortingHat.house_designation(a)
            self.assertEqual(corr_ans, stu_ans, ans.format(a))

    def test_designation(self):
        qualities = ['bold', 'wise', 'curious', 'smart', 'cunning', 'loyal', 'patient', 'brave', 'pretty', 'wily']
        a = [[random.choice(qualities) for _ in range(3)] for _ in range(5)]
        ans = _("Should you really belong to this house? \n"
                "Your returned {}, wasn't there an order more suited for the qualities {}?")
        for i in range(len(a)):
            corr_ans = corr.house_designation(a[i])
            stu_ans = sortingHat.house_designation(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, a[i]))


if __name__ == '__main__':
    unittest.main()
