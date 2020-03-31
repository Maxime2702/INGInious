#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQbf02 as corr
import qbf02
import sys
from contextlib import redirect_stdout
import io


class TestQBF(unittest.TestCase):
    def test_qbf(self):
        ans = _("Les diviseurs des entiers avant {} sont:\n{}\n et vous avez renvoyé:\n{}")
        for i in  [11] + [random.randint(1, 20) for _ in range(5)] + [1]:
            with io.StringIO() as out, redirect_stdout(out):
                qbf02.qbf(i)
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.qbf(i)
                corr_ans = out.getvalue()
            if corr_ans != stu_ans:
                self.fail(ans.format(i, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__
