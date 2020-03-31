#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import string
import random
import unicodedata

import CorrAmazonPay as corr
import amazon


class TestAmazonPay(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(amazon, "pay_employee"), _("The function `pay_employee` does not exist."))

    def basic_case(self):
        sal = random.randint(10, 16)
        hours = random.randint(20, 300)
        emp = amazon.Employee(sal)
        empCorr = corr.Employee(sal)
        corr.pay_employee(empCorr, hours)
        amazon.pay_employee(emp, hours)
        ans = _("your function pay_employees does not give the good salary to the employee, "
                "should be {} and you give {}")
        self.assertEqual(emp.money, empCorr.money, ans.format(emp.money, empCorr.money))

    def test_exceptions(self):
        emp = amazon.Employee(10)
        empNeg = amazon.Employee(-1)
        empTooMuch = amazon.Employee(101)
        with self.assertRaises(amazon.EmployeeDidntWorked, msg=_("the employee did not work, you should raise an"
                                                                 " exception")):
            amazon.pay_employee(emp, 0)
        with self.assertRaises(amazon.EmployeeWorkedNegatively, msg=_("the employee worked negatively, you should raise"
                                                                      " an exception")):
            amazon.pay_employee(emp, -1)
        with self.assertRaises(amazon.EmployeeWorkedTooMuch, msg=_("the employee worked too much, you should raise an"
                                                                   " exception")):
            amazon.pay_employee(emp, 745)
        with self.assertRaises(amazon.PayIsNegative, msg=_("the employee is payed negatively, you should raise an"
                                                           " exception")):
            amazon.pay_employee(empNeg, 30)
        with self.assertRaises(amazon.PayIsTooBig, msg=_("the employee is payed negatively, you should raise an"
                                                         " exception")):
            amazon.pay_employee(empTooMuch, 30)


if __name__ == '__main__':
    unittest.main()
