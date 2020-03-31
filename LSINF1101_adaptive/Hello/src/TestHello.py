#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import string

import CorrHello as corr
import hello


class TestHello(unittest.TestCase):
    def test_example(self):
        ans = _('When "Charles" is the user\'s name, ``hello`` contains "{}" instead of "Hello, Charles!"')
        student_ans = hello.say_hello("Charles")
        self.assertEqual("Hello, Charles!", student_ans, ans.format(student_ans))

    def test_names(self):
        names = ["Kim", "Siegfried", "Johnny"]
        ans = _('When "{0}" is the user\'s name, ``hello`` contains "{1}" instead of "Hello, {0}!"')
        for i in range(len(names)):
            student_ans = hello.say_hello(names[i])
            self.assertEqual("Hello, {}!".format(names[i]), student_ans, ans.format(names[i], student_ans))

    def test_random(self):
        random_name = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        ans = _('When "{0}" is the user\'s name, ``hello`` contains "{1}" instead of "Hello, {0}!"')
        student_ans = hello.say_hello(random_name)
        self.assertEqual("Hello, {}!".format(random_name), student_ans, ans.format(random_name, student_ans))


if __name__ == '__main__':
    unittest.main()
