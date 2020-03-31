#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import timeout_decorator

import CorrFibonacci as corr
import fibonacci


class Counter(object):
    def __init__(self, fun):
        self._fun = fun
        self.counter = 0

    def __call__(self,*args, **kwargs):
        self.counter += 1
        return self._fun(*args, **kwargs)


class TestFactorial(unittest.TestCase):
    def setUp(self):
        a = random.randint(6, 30)
        ans = _("You did not use recursion in your algorithm.")
        fibonacci.fibo = Counter(fibonacci.fibo)
        stu_ans = fibonacci.fibo(a)
        self.assertNotEqual(1, fibonacci.fibo.counter, ans)

    def test_fibonacci(self):
        a = [random.randint(6, 20) for _ in range(5)]
        ans = _("The {}th fibonacci number is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = fibonacci.fibo(a[i])
            corr_ans = corr.fibonacci(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_zero(self):
        ans = _("For 0 the fibonacci number is 0 and you returned {}.")
        stu_ans = fibonacci.fibo(0)
        self.assertEqual(0, stu_ans, ans.format(stu_ans))

    def test_one(self):
        ans = _("For 1 the fibonacci number is 1 and you returned {}.")
        stu_ans = fibonacci.fibo(1)
        self.assertEqual(1, stu_ans, ans.format(stu_ans))

    @timeout_decorator.timeout(1, exception_message=_("There can not be a number in a negative place in a sequence,"
                                                        " you should have returned None."))
    def test_negatives(self):
        a = [-(random.randint(1, 100)) for _ in range(5)]
        ans = _("There can not be a number in a negative place in a sequence, you should have returned None.")
        for i in range(len(a)):
            try:
                stu_ans = fibonacci.fibo(a[i])
                self.assertEqual(None, stu_ans, ans)
            except RecursionError:
                self.assertFalse(True, ans)


if __name__ == '__main__':
    unittest.main()
