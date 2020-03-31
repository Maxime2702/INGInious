#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrRemainder as corr
import remainder


class MyInt(int):
    def __mod__(self, other):
        raise AttributeError(_("Nice try! But the operator '%' has been disabled.\n"
                              "\t\tPlease write an actual algorithm calculating the remainder."))

    def __int__(self):
        return self

    def __float__(self):
        return self


class TestRemainder(unittest.TestCase):
    def test_remainder(self):
        a = [random.randint(1, 100) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        ans = _("The remainder of the entire division {} / {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = remainder.remainder(MyInt(a[i]), MyInt(b[i]))
            corr_ans = corr.remainder(a[i], b[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], b[i], corr_ans, stu_ans))
            
    def test_under(self):
        a = [random.randint(1, 20) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        ans = _("The remainder of the entire division {} / {} is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = remainder.remainder(MyInt(a[i]), MyInt(b[i]))
            corr_ans = corr.remainder(a[i], b[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], b[i], corr_ans, stu_ans))

    def test_zero(self):
        a = random.randint(1, 100)
        b = 0
        ans = _("The remainder of the entire division {} / {} is None and you returned {}.")
        stu_ans = remainder.remainder(MyInt(a), MyInt(b))
        self.assertEqual(None, stu_ans, ans.format(a, b, stu_ans))


if __name__ == '__main__':
    unittest.main()
