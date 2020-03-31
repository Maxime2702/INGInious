#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import string
import random
import unicodedata

import CorrAmazon as corr
import amazon


class TestStudent(unittest.TestCase):
    def test_exist(self):
        self.assertTrue((hasattr(amazon, '__init__') and hasattr(amazon, '__str__')),
                        _("You did not provide the init or str methods."))

    def test_str(self):
        id_buyer = random.randint(0, 100)
        id_item = random.randint(0, 100)
        price = random.randint(0, 100)
        quantity = random.randint(0, 100)
        ans = _("With the following data: {}, {}, {}, {} for the command created, you returned {} instead of {}")
        stu_ans = amazon.Command(id_buyer, id_item, price, quantity)
        corr_ans = corr.Command(id_buyer, id_item, price, quantity)
        self.assertEqual(str(corr_ans), str(stu_ans), ans.format(id_buyer, id_item, price, quantity, stu_ans, corr_ans))

    def test_helper(self):
        id_buyer = random.randint(0, 100)
        id_item = random.randint(0, 100)
        price = random.randint(0, 100)
        quantity = random.randint(0, 100)
        number = random.randint(10, 100)
        last_command = None
        total_price = 0
        for i in range(0, number):
            last_command = amazon.Command(id_buyer, id_item, price, quantity)
            total_price += price*quantity
        self.assertEqual(number, last_command.get_number_total_command(), msg=_("you do not get the correct number "
                                                                                "of Command"))
        self.assertEqual(total_price, last_command.get_total_price(), msg=_("you do not get the correct total price "
                                                                            "of all Command"))
        
    def test_class(self):
        try:
            amazon.Command.get_number_total_command()
            amazon.Command.get_total_price()
        except TypeError:
            self.fail("Vos méthodes de classes disposent-elles bien du décorateur @classmethod?")


if __name__ == '__main__':
    unittest.main()
