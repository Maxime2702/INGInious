#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import inspect
import ast

import CorrSort as corr
import sorter


class TestSort(unittest.TestCase):
    def test_use_sort(self):
        ans = _("Nice try! But using the predefined 'sort' function is a bit of cheating.\n\t\tTry to implement an actual algorithm for sorting the list.")
        file_ast = ast.parse(inspect.getsource(sorter.sorter))
        tree = ast.walk(file_ast)
        if 'sort' in [f.func.attr for f in tree if isinstance(f, ast.Call) and not isinstance(f.func, ast.Name)]:
            self.fail(ans)
    
    def test_sort(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sorted version of {} is {} and you returned {}.")
        for l in lists:
            stu_ans = sorter.sorter(l.copy())
            corr_ans = sorted(l.copy())
            self.assertEqual(corr_ans, stu_ans, ans.format(l, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
