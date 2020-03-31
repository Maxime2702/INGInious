#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import CorrMax as corr
import max


class TestMax(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(max, 'afficheMax'), _("You did not provide the requested method."))

    def test_max(self):
        a = [random.randint(1, 100) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        ans = _("Le maximum de {} est {} et vous avez renvoyé {}.")
        for i in range(len(a)):
            with io.StringIO() as out, redirect_stdout(out):
                max.afficheMax(a[i], b[i])
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.maximum(a[i], b[i])
                corr_ans = out.getvalue()
            self.assertEqual(corr_ans, stu_ans, ans.format([a[i], b[i]], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
