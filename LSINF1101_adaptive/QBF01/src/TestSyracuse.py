#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrSyracuse as corr
import syracuse
import sys
from contextlib import redirect_stdout
import io


class TestSyracuse(unittest.TestCase):
    def test_syracuse(self):
        ans = _("The syracuse function of {} is:\n{}\nand you returned:\n{}")
        for i in  [11] + [random.randint(1, 50) for _ in range(5)] + [1]:
            with io.StringIO() as out, redirect_stdout(out):
                syracuse.syracuse(i)
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.syracuse(i)
                corr_ans = out.getvalue()
            if corr_ans != stu_ans:
                self.fail(ans.format(i, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__
