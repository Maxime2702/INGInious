#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import timeout_decorator
import ast

import CorrQBF as corr
import qbf


class Testqbf(unittest.TestCase):               
    def setUp(self):
        ans = ("Les boucles ne sont pas autorisées pour cet exercices.")
        with open('qbf.py', 'r') as f:
            s = f.read()
            if [x for x in ast.walk(ast.parse(s)) if isinstance(x, (ast.For, ast.While))]:
                self.fail(ans)
    
    def test_exist_fib(self):
        self.assertTrue(hasattr(qbf, 'fib'), _("You did not name the method as expected."))
        
    def test_fibo(self):
        a = [random.randint(1, 15) for _ in range(5)]
        ans = _("The {}th fibonacci number is {} and you returned {}.")
        for e in a:
            stu_ans = qbf.fib(e)
            corr_ans = corr.fib(e)
            self.assertEqual(corr_ans, stu_ans, ans.format(e, corr_ans, stu_ans))

    @timeout_decorator.timeout(1, exception_message= _("It seems that you didn't use the memoization properly."))
    def test_high_comput_time(self):
        a = 500
        ans = _("The {}th fibonacci number is {} and you returned {}.")
        stu_ans = qbf.fib(a)
        corr_ans = corr.fib(a)
        self.assertEqual(corr_ans, stu_ans, ans.format(a, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
