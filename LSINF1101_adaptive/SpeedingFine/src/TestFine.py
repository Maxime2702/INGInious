#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrFine as corr
import fine


class TestFine(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(fine, 'fine'), _("You did not name the method as expected."))

    def test_over_10_fine(self):
        a = [30, 50, 70, 90, 120]
        ans = _("The speed fine for a speed of {} instead of {} is {} and you returned {}.")
        for i in range(len(a)):
            b = a[i] + random.randint(11, 40)
            stu_ans = fine.fine(a[i], b)
            corr_ans = corr.fine(a[i], b)
            self.assertEqual(corr_ans, stu_ans, ans.format(str(b), str(a[i]), str(corr_ans), str(stu_ans)))

    def test_under_10_fine(self):
        a = [30, 50, 70, 90, 120]
        ans = _("The speed fine for a speed of {} instead of {} is {} and you returned {}.")
        for i in range(len(a)):
            b = a[i] + random.randint(3, 10)
            stu_ans = fine.fine(a[i], b)
            corr_ans = corr.fine(a[i], b)
            self.assertEqual(corr_ans, stu_ans, ans.format(str(b), str(a[i]), str(corr_ans), str(stu_ans)))

    def test_min_fine(self):
        a = [30, 50, 70, 90, 120]
        ans = _("The speed fine for a speed of {} instead of {} is {} and you returned {}.")
        for i in range(len(a)):
            b = a[i] + random.randint(1, 2)
            stu_ans = fine.fine(a[i], b)
            corr_ans = corr.fine(a[i], b)
            self.assertEqual(corr_ans, stu_ans, ans.format(str(b), str(a[i]), str(corr_ans), str(stu_ans)))

    def test_no_trespassing(self):
        a = [30, 50, 70, 90, 120]
        ans = _("The speed fine for a speed of {} instead of {} is {} and you returned {}.")
        for i in range(len(a)):
            b = a[i] - random.randint(0, 1)
            stu_ans = fine.fine(a[i], b)
            corr_ans = corr.fine(a[i], b)
            self.assertEqual(corr_ans, stu_ans, ans.format(str(b), str(a[i]), str(corr_ans), str(stu_ans)))


if __name__ == '__main__':
    unittest.main()
