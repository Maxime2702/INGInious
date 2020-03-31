#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrTriangle as corr
import triangle as stu


class TestTriangle(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(True, "triangle" in dir(stu), _("You did not name the method as expected."))
    def test_triangle(self):
        inputs = [random.randint(0, 100) for _ in range(random.randint(1, 20))]
        inputs[0] = 10
        ans = _("\nFor n = {}, the expected triangle is: \n {} but you returned: \n{}.")
        for i in range(len(inputs)):
            stu_ans = stu.triangle(inputs[i])
            corr_ans = corr.triangle(inputs[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(inputs[i], corr_ans, stu_ans))

if __name__ == '__main__':
    unittest.main()
