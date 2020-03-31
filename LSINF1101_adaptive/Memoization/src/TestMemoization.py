#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import timeout_decorator

import CorrMemoization as corr
import memoization


class TestExtractor(unittest.TestCase):
    def test_exist_memo(self):
        self.assertTrue(hasattr(memoization, 'memoization'), "@1@: " + _("You did not name the method as expected."))

    def test_exist_fibo(self):
        self.assertTrue(hasattr(memoization, 'fibonacci'), "@2@: " + _("You did not name the method as expected."))

    def test_exist_fact(self):
        self.assertTrue(hasattr(memoization, 'factorial'), "@3@: " + _("You did not name the method as expected."))

    def test_memoize(self):
        a = [random.randint(1, 15) for _ in range(5)]
        ans = "@1@: " + _("The sum of the {}th first numbers is {} and you returned {}. Your memoization algorithm "
                           "seem to not support other functions.")
        for i in range(len(a)):
            stu_ans = memoization.memoization(memoization.n_sum, a[i])
            corr_ans = corr.memoization(corr.n_sum, a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_fibo(self):
        a = [random.randint(1, 15) for _ in range(5)]
        ans = "@2@: " + _("The {}th fibonacci number is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = memoization.fibonacci(a[i])
            corr_ans = corr.memoization(corr.fibonacci, a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_fact(self):
        a = [random.randint(1, 15) for _ in range(5)]
        ans = "@3@: " + _("The factorial of {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = memoization.factorial(a[i])
            corr_ans = corr.memoization(corr.factorial, a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    @timeout_decorator.timeout(1, exception_message="@0@: " + _("It seems that you didn't use the memoization "
                                                                 "properly."))
    def test_high_comput_time(self):
        a = 500
        ans = "@2@: " + _("The {}th fibonacci number is {} and you returned {}.")
        stu_ans = memoization.memoization(memoization.fibonacci, a)
        corr_ans = corr.memoization(corr.fibonacci, a)
        self.assertEqual(corr_ans, stu_ans, ans.format(a, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
