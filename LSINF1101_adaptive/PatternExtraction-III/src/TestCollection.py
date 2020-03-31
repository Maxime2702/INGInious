#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrCollection as corr
import collection


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


def generate_intel(file):
    with open(file, 'w+') as f:
        for _ in range(random.randint(16, 50)):
            f.write(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32)))


class TestCollection(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(collection, 'collect'), _("You did not name the method as expected."))

    def test_collect(self):
        generate_intel('data.txt')
        ans = _("The dictionary expected of the given file is {} and you returned {}.")
        stu_ans = collection.collect('data.txt')
        corr_ans = corr.collect('data.txt')
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))

    def test_IOError(self):
        self.assertRaises(IOError, collection.collect, 'IOError.txt')


if __name__ == '__main__':
    unittest.main()
