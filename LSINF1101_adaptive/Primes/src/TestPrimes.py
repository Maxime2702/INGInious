#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest

import CorrPrimes as corr
import primes
import ast

class TestPrimes(unittest.TestCase):               
    def test_exist(self):
        self.assertTrue(hasattr(primes, 'primes'), _("You did not name the method as expected."))

    def test_primes(self):
        a = [2, 70]
        ans = _("The prime numbers with a maximum value of {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = primes.primes(a[i])
            corr_ans = corr.primes(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_not_prime_case(self):
        a = [0, 1]
        ans = _("The prime numbers with a maximum value of {} is {} and you returned {}. \n You should check the conditions to be a prime number.")
        for i in range(len(a)):
            stu_ans = primes.primes(a[i])
            corr_ans = corr.primes(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))

    def test_negative_case(self):
        a = [-40, -2]
        ans = _("The prime numbers with a maximum value of {} is {} and you returned {}. \n You should check the conditions to be a prime number.")
        for i in range(len(a)):
            stu_ans = primes.primes(a[i])
            corr_ans = corr.primes(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
