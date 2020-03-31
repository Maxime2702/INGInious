#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata

import CorrQuetelet as corr
import quetelet


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestQuetelet(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(quetelet, 'quetelet'), _("You did not name the method as expected."))

    def test_bounds(self):
        a = [2.0, 1.5, 1.5]
        b = [80, 56.25, 67.5]
        ans = _("The quetelet index with a height of {} and a weight of {} is {} and you returned {}. \n You should watch the bounds of your conditions.")
        for i in range(len(a)):
            stu_ans = quetelet.quetelet(a[i], b[i])
            corr_ans = corr.quetelet(a[i], b[i])
            self.assertEqual(equal_string(corr_ans), equal_string(stu_ans), ans.format(a[i], b[i], corr_ans, stu_ans))

    def test_quetelet(self):
        a = [2.1, 1.87, 1.5, 1.6]
        b = [80, 300, 50, 70]
        ans = _("The quetelet index with a height of {} and a weight of {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = quetelet.quetelet(a[i], b[i])
            corr_ans = corr.quetelet(a[i], b[i])
            self.assertEqual(equal_string(corr_ans), equal_string(stu_ans), ans.format(a[i], b[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
