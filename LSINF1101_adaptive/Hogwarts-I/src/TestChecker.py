#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import string

import CorrChecker as corr
import passwordChecker


class TestChecker(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(passwordChecker, 'portrait'), _("You did not name the method as expected."))

    def test_is(self):
        a = 'test'
        b = ''.join(['t', 'e', 's', 't'])
        ans = _("Are you really belonging to this house? \n Watch if you're really checking the equality there.")
        stu_ans = passwordChecker.portrait(a, b)
        self.assertTrue(stu_ans, ans)

    def test_checker(self):
        a = [''.join(random.choice(string.ascii_letters) for _ in range(10)) for _ in range(5)]
        b = [e + 'a' for e in a]
        a.append('caput draconis')
        b.append('caput draconis')
        ans = _("Are you really belonging to this house? \n"
                " With the right and entered password being {} and {}  you compared  them as {}ly identical.")
        for i in range(len(a)):
            stu_ans = passwordChecker.portrait(a[i], b[i])
            corr_ans = corr.check(a[i], b[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], b[i], stu_ans))


if __name__ == '__main__':
    unittest.main()
