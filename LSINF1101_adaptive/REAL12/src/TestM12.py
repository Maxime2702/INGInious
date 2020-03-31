#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

import mission12


class TestM12(unittest.TestCase):
    def test_exist_class(self):
        self.assertTrue(hasattr(mission12, "ImageFolder"), "Vous n'avez pas créé la classe ImageFolder comme demandé.")
                   
    def test_exist_func_mission12(self):
        for fun in ['__init__', 'next', 'read_ascii']:
            self.assertTrue(hasattr(classement.ImageFolder, fun), "Vous n'avez pas créé la fonction {} de la classe ImageFolder comme demandé.".format(fun))


if __name__ == '__main__':
    unittest.main()

