#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrCarre as corr
import carre as stu


class TestCarre(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(True, "carre" in dir(stu), _("You did not name the method as expected."))
    
    def test_carre(self):
        inputs = [random.randint(0, 100) for _ in range(random.randint(1, 20))]
        inputs[0] = 10
        ans = _("\nFor n = {}, the expected carre is: \n {} but you returned: \n{}.")
        for i in range(len(inputs)):
            stu_ans = stu.carre(inputs[i])
            corr_ans = corr.carre(inputs[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(inputs[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
