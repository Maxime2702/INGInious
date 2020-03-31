#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import timeout_decorator
import ast

import CorrM08 as corr
import memoisation


class Counter(object):
    def __init__(self, fun):
        self._fun = fun
        self.counter = 0

    def __call__(self,*args, **kwargs):
        self.counter += 1
        return self._fun(*args, **kwargs)


class TestM08(unittest.TestCase):      
    def setUp(self):
        a = random.randint(6, 30)
        ans = _("Vous n'avez pas utilisé la récursion dans la fonction fibo.")
        memoisation.fibo = Counter(memoisation.fibo)
        stu_ans = memoisation.fibo(a)
        self.assertNotEqual(1, memoisation.fibo.counter, ans)
    
    def test_exist_fibo(self):
        self.assertTrue(hasattr(memoisation, 'fibo'), "Vous n'avez pas nommé la fonction récursive comme demandée.")
    
    def test_exist_fibonacci(self):
        self.assertTrue(hasattr(memoisation, 'fibonacci'), "Vous n'avez pas nommé la fonction itérative comme demandée.")
    
    def test_exist_fibo_mem(self):
        self.assertTrue(hasattr(memoisation, 'fibo_mem'), "Vous n'avez pas nommé la fonction mémoïzée comme demandée.")
    
    def test_exist_memoization(self):
        self.assertTrue(hasattr(memoisation, 'memoization'), "Vous n'avez pas nommé la fonction de mémoïzation comme demandée.")
        
    def test_fibo(self):
        a = [random.randint(1, 15) for _ in range(5)]
        ans = "Pour votre fonction révursive:\n" + _("The {}th fibonacci number is {} and you returned {}.")
        for e in a:
            stu_ans = memoisation.fibo(e)
            corr_ans = corr.fibo(e)
            self.assertEqual(corr_ans, stu_ans, ans.format(e, corr_ans, stu_ans))
        
    def test_fibonacci(self):
        a = [random.randint(1, 15) for _ in range(5)]
        ans = "Pour votre fonction itérative:\n" + _("The {}th fibonacci number is {} and you returned {}.")
        for e in a:
            stu_ans = memoisation.fibonacci(e)
            corr_ans = corr.fibonacci(e)
            self.assertEqual(corr_ans, stu_ans, ans.format(e, corr_ans, stu_ans))
        
    def test_fibo_mem(self):
        a = [random.randint(1, 15) for _ in range(5)]
        ans = "Pour votre fonction mémoïzée:\n" + _("The {}th fibonacci number is {} and you returned {}.")
        for e in a:
            stu_ans = memoisation.memoization(memoisation.fibo_mem, e)
            corr_ans = corr.memoization(corr.fibo_mem, e)
            self.assertEqual(corr_ans, stu_ans, ans.format(e, corr_ans, stu_ans))

    @timeout_decorator.timeout(1, exception_message= _("It seems that you didn't use the memoization properly."))
    def test_high_comput_time(self):
        a = 500
        ans = "Pour votre fonction mémoïzée:\n" + _("The {}th fibonacci number is {} and you returned {}.")
        stu_ans = memoisation.memoization(memoisation.fibo_mem, a)
        corr_ans = corr.memoization(corr.fibo_mem, a)
        self.assertEqual(corr_ans, stu_ans, ans.format(a, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()


