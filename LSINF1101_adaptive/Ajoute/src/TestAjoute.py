#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrAjoute as corr
import ajoute as stu


class TestAjoute(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(True, "ajoute" in dir(stu), _("You did not name the method as expected."))
    
    def test_given(self):
        ans = _("With l={}, the expected list after ajoute(l,{}) is: \n {} but you returned: \n{}.")
        l = [ 3, 1, 5, 4 ]
        stu.ajoute ( l, 4 )
        corr_ans = [ 3, 1, 5, 4 ]
        self.assertEqual(corr_ans, l, ans.format(l, 4, corr_ans, l))

        l = [ 3, 1, 5, 4 ]
        stu_ans = stu.ajoute ( l, 6 )
        corr_ans = [ 3, 1, 5, 4, 6 ]
        self.assertEqual(corr_ans, l, ans.format(l, 6, corr_ans, l))

        l = [ 3, 1, 5, 4, 6 ]
        stu_ans = stu.ajoute ( l, 7 )
        corr_ans = [ 3, 1, 5, 4, 6, 7 ]
        self.assertEqual(corr_ans, l, ans.format(l, 7, corr_ans, l))

        l = [ 3, 1, 5, 4, 6, 7 ]
        stu_ans = stu.ajoute ( l, 6 )
        corr_ans = [ 3, 1, 5, 4, 6, 7 ]
        self.assertEqual(corr_ans, l, ans.format(l, 6, corr_ans, l))

if __name__ == '__main__':
    unittest.main()
