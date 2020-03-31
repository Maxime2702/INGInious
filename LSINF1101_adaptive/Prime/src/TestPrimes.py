#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrPrimes as corr
import primes


class TestPrimes(unittest.TestCase):

    def test_primes(self):
        i = random.randint(1, 100) 
        ans = _("Pour le nombre {}, il aurait fallu mettre {} dans ``is_prime`` et vous y avez stocké {}.")
        stu_ans = primes.prime(i)
        corr_ans = corr.prime(i)
        self.assertEqual(corr_ans, stu_ans, ans.format(i, corr_ans, stu_ans))

    def test_not_prime_case(self):
        i = 6
        ans = _("Pour le nombre {}, il aurait fallu mettre ``False`` dans ``is_prime`` et vous y avez stocké {}.")
        stu_ans = primes.prime(i)
        self.assertFalse(stu_ans, ans.format(i, stu_ans))

    def test_prime_case(self):
        i = 3
        ans = _("Pour le nombre {}, il aurait fallu mettre ``True`` dans ``is_prime`` et vous y avez stocké {}.")
        stu_ans = primes.prime(i)
        self.assertTrue(stu_ans, ans.format(i, stu_ans))


if __name__ == '__main__':
    unittest.main()
