#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

import CorrBath as corr
import bath as stu


class TestBath(unittest.TestCase):
    def test_filled_time(self):
        try:
            self.assertAlmostEqual(stu.filled_time,corr.filled_time,msg=_("You don't have the good answer when computing the time to fill the bathtub ({}min).".format(stu.filled_time)))
            #if corr.filled_time != stu.filled_time:  # Don't give the answer ("<answer> is not <student answer>")
            #    self.fail(_("You don't have the good answer when computing the time to fill the bathtub ({}min).".format(stu.filled_time)))
        except (NameError, AttributeError):
            self.fail(_("You did not name the variable `filled_time` correctly (is it out of the `for` loop?)"))

    def test_water_vol(self):
        try:
            if corr.water_vol != stu.water_vol:  # Don't give the answer ("<answer> is not <student answer>")
                self.fail(_("You did not compute the right value for the volume of water ({}L). Did you do the right number of iterations?").format(stu.water_vol))
        except (NameError, AttributeError):
            self.fail(_("You did not name the variable `water_vol` correctly."))


if __name__ == '__main__':
    unittest.main()
