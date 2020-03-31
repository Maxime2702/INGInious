#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestQ(unittest.TestCase):
    def test_exist_files(self):
        self.assertEqual(1, q.plus_frequent([1, 1, 2, 3]), "test")


if __name__ == '__main__':
    unittest.main()
