#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

import CorrM11 as corr
import classement


class TestM11(unittest.TestCase):
    def test_exist_class(self):
        self.assertTrue(hasattr(classement, "OrderedLinkedList"), "Vous n'avez pas créé la classe OrderedLinkedList comme demandé.")
                   
    def test_exist_func_classement(self):
        for fun in ['__init__', 'size', 'add', 'get', 'get_position', 'remove', '__str__']:
            self.assertTrue(hasattr(classement.Classement, fun), "Vous n'avez pas créé la fonction {} de la classe Classement comme demandé.".format(fun))
        

if __name__ == '__main__':
    unittest.main()

