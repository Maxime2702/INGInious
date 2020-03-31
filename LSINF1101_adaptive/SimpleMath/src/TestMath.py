#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import CorrMath as corr
import math_temp


class TestFactorial(unittest.TestCase):
    def test_math(self):
        ans = _("Le résultat attendu était {} et vous avez printé {}.")
        with io.StringIO() as out, redirect_stdout(out):
            math_temp.q_math()
            stu_ans = out.getvalue()
        with io.StringIO() as out, redirect_stdout(out):
            corr.q_math()
            corr_ans = out.getvalue()
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))

if __name__ == '__main__':
    unittest.main()
