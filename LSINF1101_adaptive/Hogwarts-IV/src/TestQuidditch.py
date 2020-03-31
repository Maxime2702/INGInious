#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random

import CorrQuidditch as corr
import quidditch


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


def generate_intel(file, passed_end=False):
    with open(file, 'w+') as f:
        f.write('A' + '\n')
        f.write('B' + '\n')
        for _ in range(random.randint(6, 10)):
            f.write(random.choice(['A', 'B']) + ' 10' + '\n')
        f.write(random.choice(['A', 'B']) + ' 150' + '\n')
        if passed_end: f.write(random.choice(['A ', 'B ']) + str(random.randrange(10, 250)) + '\n')


class TestQuidditch(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(quidditch, 'referee'), _("You did not name the method as expected."))

    def test_referee(self):
        generate_intel('data.txt')
        ans = _("Did the bludger hit you too hard? For the given score {} you decided {} won.")
        stu_ans = quidditch.referee('data.txt')
        corr_ans = corr.referee('data.txt')
        with open('data.txt', 'r') as f:
            score = f.readlines()
        self.assertEqual(corr_ans, stu_ans, ans.format(score, stu_ans))

    def test_passed_end(self):
        generate_intel('data.txt', True)
        ans = _("Did the bludger hit you too hard? The match is supposed to end after the caught of the golden snitch.")
        stu_ans = quidditch.referee('data.txt')
        corr_ans = corr.referee('data.txt')
        with open('data.txt', 'r') as f:
            score = f.readlines()
        self.assertEqual(corr_ans, stu_ans, ans)

    def test_IOError(self):
        self.assertRaises(IOError, quidditch.referee, 'IOError.txt')


if __name__ == '__main__':
    unittest.main()
