#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import os.path

import CorrLoadSave as corr
import loadSave


class TestLoadSave(unittest.TestCase):

    def test_create_file(self):
        filename = "test1.txt"
        loadSave.save_data(filename, 10, 10, 10, 10)
        self.assertTrue(os.path.isfile(filename), msg=_("You don't even create a file... This is a bit annoying for "
                                                        "a saving function"))

    def test_missing_file(self):
        filename = "test0.txt"
        with self.assertRaises(FileNotFoundError, msg=_("the player can't start a new game, and is very sad... "
                                                        "Check that the file exist")):
            loadSave.load_data(filename)

    def test_save_load_data(self):
        filename = "test2.txt"
        loadSave.save_data(filename, 10, 10, 10, 10)
        self.assertTrue(os.path.isfile(filename), msg=_("You don't even create a file... This is a bit annoying for a "
                                                        "saving function"))
        self.assertEqual(loadSave.load_data(filename), (10, 10, 10, 10), msg=_("The player loaded the wrong value."))

    def test_save_load_data_random(self):
        filename = "test3.txt"
        (life, mana, x, y) = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
                              random.randint(0, 100))
        loadSave.save_data(filename, life, mana, x, y)
        self.assertTrue(os.path.isfile(filename), msg=_("You don't even create a file... This is a bit annoying for a "
                                                        "saving function"))
        self.assertEqual(loadSave.load_data(filename), (life, mana, x, y), msg=_("The player loaded the wrong value."))


if __name__ == '__main__':
    unittest.main()
