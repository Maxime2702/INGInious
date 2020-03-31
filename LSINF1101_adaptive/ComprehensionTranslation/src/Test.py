#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest

import Corr as corr
import comp
import ast

class TestPrimes(unittest.TestCase):
    def test_no_list_comp(self):
        with open('comp.py', 'r') as f:
            s = f.read()
            if [x for x in ast.walk(ast.parse(s)) if isinstance(x, ast.ListComp)]:
                ans = _("It is forbidden to use a list comprehension in this exercise.")
                self.fail(ans)
            if not [x for x in ast.walk(ast.parse(s)) if isinstance(x, ast.For)]:
                ans = _("You must use a for loop in this exercise.")
                self.fail(ans)

    def test_content(self):
        ans = _("The expected list was {} and you returned {}.")
        stu_ans = comp.exe()
        corr_ans = corr.exe()
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
