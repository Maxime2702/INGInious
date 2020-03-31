#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import string

import CorrHighOrder as corr
import highOrder


class TestHighOrder(unittest.TestCase):
    def test_lambda(self):
        x = random.randint(10, 100)
        stud_ans = highOrder.mult_table(x)
        for n in range(3):
            self.assertEqual(stud_ans[n].__name__, '<lambda>', "Use lambda and not functions.")
    
    def test_rand(self):
        ans = _("The function {} with the argument {} of the list\n gives {} when the answer should be {}.\n "
                "You may have not captured the variable in the lambda. (see in the instructions)")
        for m in range(5):
            x = random.randint(10, 100)
            stud_ans = highOrder.mult_table(x)
            for n in range(3):
                i = random.randint(0, x)
                j = random.randint(0, 1000)
                k = stud_ans[i](j)
                self.assertEqual(i*j, k, ans.format(i, j, k, i*j))
                
    def test_length(self):
        ans = _("The length of the list is {} and it should be {}.")
        for m in range(5):
            x = random.randint(10, 100)
            stud_ans = highOrder.mult_table(x)
            self.assertEqual(x+1, len(stud_ans), ans.format(len(stud_ans), x))

