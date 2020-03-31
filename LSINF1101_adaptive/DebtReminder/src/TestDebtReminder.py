#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrDebtReminder as corr
import debts as stu

class TestDebtReminder(unittest.TestCase):
    def check_existences(self):
        try:
            if type(corr.borrowed_money) != dict:
                self.assertTrue(False, _("`borrowed_money` must be of type `dict`."))
        except NameError:
            self.assertTrue(False, _("The variable `borrowed_money` doesn't exist."))
        self.assertTrue(hasattr(stu, "give_money"), _("The function `give_money` does not exist."))
        self.assertTrue(hasattr(stu, "total_money_borrowed"), _("The function `total_money_borrowed` does not exist."))

    def test_give_money_total_valid(self):
        self.check_existences()
        name1 = "Paul"; name2 = "John"; name3 = "Georges"; name4 = "Ringo"
        correct_ans = {}
        student_ans = {}
        try:
            corr.give_money(correct_ans, name1, name2, 10)
            stu.give_money(student_ans, name1, name2, 10)
            corr.give_money(correct_ans, name2, name3, 12)
            stu.give_money(student_ans, name2, name3, 12)
            corr.give_money(correct_ans, name2, name1, 10.5)
            stu.give_money(student_ans, name2, name1, 10.5)
            corr.give_money(correct_ans, name1, name4, 0.25)
            stu.give_money(student_ans, name1, name4, 0.25)
            random_int = random.randint(1, 20)
            corr.give_money(correct_ans, name4, name3, random_int)
            stu.give_money(student_ans, name4, name3, random_int)
            self.assertEqual(correct_ans, student_ans, _("After 5 transactions between 4 people, you got {} instead of {}.".format(student_ans, correct_ans)))
            corr_tot = corr.total_money_borrowed(correct_ans)
            student_tot = stu.total_money_borrowed(student_ans)
            self.assertEqual(corr_tot, student_tot, _("With {}, you computed a total amount of money borrowed of {} instead of {}.".format(student_ans, student_tot, corr_tot)))
        except Exception as e:
            msg = _("You wrongly raised an exception while using `give_money()` or `total_money_borrowed()` with valid arguments: {}('{}')".format(type(e).__name__, e))
            self.fail(msg)

    def test_give_money_invalid(self):
        self.check_existences()
        try:
            valid_dict = {}
            valid_names = ["laurel", "hardy"]
            valid_amount = 1
            invalid_param = ["slt", ValueError()]
            invalid_names = [42, -12.05, ValueError()]
            for dictionary in invalid_param:
                self.assertRaises(ValueError, stu.give_money, dictionary, valid_names[0], valid_names[1], valid_amount)
            for name in invalid_names:
                self.assertRaises(ValueError, stu.give_money, valid_dict, name, valid_names[0], valid_amount)
                self.assertRaises(ValueError, stu.give_money, valid_dict, valid_names[1], name, valid_amount)
            for amount in invalid_param:
                self.assertRaises(ValueError, stu.give_money, valid_dict, valid_names[0], valid_names[1], amount)
            self.assertRaises(ValueError, stu.give_money, valid_dict, valid_names[0], valid_names[0], valid_amount)
        except Exception as e:
            msg = _("You wrongly raised an exception while using `give_money()` with invalid arguments: {}('{}')".format(type(e).__name__, e))
            self.fail(msg)

    def test_total_invalid(self):
        self.check_existences()
        invalid_dict = ["slt", ValueError()]
        for dictionary in invalid_dict:
            try:
                self.assertRaises(ValueError, stu.total_money_borrowed, dictionary)
            except Exception as e:
                msg = _("You wrongly raised an exception while using `total_money_borrowed()` with invalid arguments: {}('{}')".format(type(e).__name__, e))
                self.fail(msg)

    def test_asked_example(self):
        self.check_existences()
        self.assertEqual(corr.borrowed_money, stu.borrowed_money, _("For the example asked, you got an incorrect answer: {}".format(stu.borrowed_money)))


if __name__ == '__main__':
    unittest.main()
