#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata

import CorrQ as corr
import q


class TestExcption(unittest.TestCase):
    def test_0_division(self):
        q.q("divide 15 0")

    def test_no_file(self):
        q.q("showfile test.txt")

    def test_Exception(self):
        self.assertRaises(Exception, q.q, 'IOError.txt', msg="Vous ne raisez pas d'exceptions pour les commandes inconnues.")


if __name__ == '__main__':
    unittest.main()
