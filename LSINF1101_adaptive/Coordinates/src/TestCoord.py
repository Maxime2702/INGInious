#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrCoord as corr
import coord

class TestFileReading(unittest.TestCase):
    def test_exist_write(self):
        self.assertTrue(hasattr(coord, 'write_coordinates'), "@1@: " + _("You did not name the method as expected."))

    def test_exist_read(self):
        self.assertTrue(hasattr(coord, 'read_coordinates'), "@2@: " + _("You did not name the method as expected."))

    def test_write(self):
        input1 = [(random.uniform(15, 19), random.uniform(1, 19))for _ in range(random.randint(2, 5))]
        ans = "@1@: " + ("Le contenu de votre fichier:\n{}\nne matche pas la liste:\n{}.")
        f = 'test.txt'
        coord.write_coordinates(f, input1)
        with open(f, 'r') as sf:
            stu_ans = sf.read().strip('\n')
        corr_ans ='\n'.join("{0},{1}".format(x,y) for x, y in input1)
        self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, input1))

    def test_ending_return(self):
        input1 = [(random.uniform(15, 19), random.uniform(1, 19))for _ in range(random.randint(2, 5))]
        f = 'test.txt'
        coord.write_coordinates(f, input1)
        with open(f, 'r') as sf:
            stu_ans = sf.read()
        corr_ans ='\n'.join("{0},{1}".format (x,y) for x, y in input1)+'\n'
        if stu_ans == corr_ans:
            self.fail("@1@: Il y a un retour à la ligne en trop dans votre fichier")      

    def test_read(self):
        input1 = [(random.uniform(15, 19), random.uniform(1, 19))for _ in range(random.randint(2, 5))]
        ans = "@2@: " + ("Le contenu du fichier:\n{}\nne matche pas la liste  que vous renvoyez:\n{}.")
        f = 'test.txt'
        text = '\n'.join("{0},{1}".format (x,y) for x, y in input1)
        with open(f, 'w+') as sf:
            sf.write(text)
        stu_ans = coord.read_coordinates(f)
        self.assertEqual(input1, stu_ans, ans.format(text, stu_ans))


if __name__ == '__main__':
    unittest.main()
