#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import ast

import CorrQ as corr
import q


class TestSieve(unittest.TestCase):               
    def setUp(self):
        ans = ("Les boucles ne sont pas autorisées pour cet exercices.")
        with open('q.py', 'r') as f:
            s = f.read()
            if [x for x in ast.walk(ast.parse(s)) if isinstance(x, (ast.For, ast.While))]:
                self.fail(ans)

    def test_exist(self):
        self.assertTrue(hasattr(q, 'sieve'), _("You did not name the method as expected."))

    def test_primes(self):
        a = [2, 70]
        ans = _("The prime numbers with a maximum value of {} is {} and you returned {}.")
        for e in a:
            stu_ans = q.sieve(e)
            corr_ans = corr.sieve(e)
            if stu_ans == [2] + corr_ans:
                self.fail("Stockes-tu les résultats de ta fonction dans une structure externe?\n Si c'est le cas, deux exécutions successives vont ajouter les deux résultats à la même liste et le second résultat ne sera donc pas correct.")
            self.assertEqual(corr_ans, stu_ans, ans.format(e, corr_ans, stu_ans))

    def test_not_prime_case(self):
        a = [0, 1]
        ans = _("The prime numbers with a maximum value of {} is {} and you returned {}. \n You should check the conditions to be a prime number.")
        for i in range(len(a)):
            stu_ans = q.sieve(a[i])
            corr_ans = corr.sieve(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
