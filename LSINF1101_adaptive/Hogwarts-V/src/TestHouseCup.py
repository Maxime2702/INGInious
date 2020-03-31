#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random

import CorrHouseCup as corr
import houseCup


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)

students = ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville', 'Cho', 'Luna', 'Sybill', 'Marcus',
            'Marietta', 'Terry', 'Penelope', 'Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton',
            'Justin', 'Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']

def generate_intel(file, winners=False):
    with open(file, 'w+') as f:
        if winners:
            f.write('Harry 150' + '\n')
            f.write('Malfoy 150')
        else:
            for _ in range(random.randint(6, 10)):
                f.write(random.choice(students) + ' ' + str(random.randrange(10, 70)) + '\n')


class TestHouseCup(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(houseCup, 'winning_house'), _("You did not name the method as expected."))

    def test_winner(self):
        generate_intel('data.txt')
        ans = _("For the given students' achievements {} you decided {} won but {} clearly did.")
        stu_ans = houseCup.winning_house('data.txt')
        corr_ans = corr.winning_house('data.txt')
        with open('data.txt', 'r') as f:
            score = f.readlines()
        self.assertEqual(corr_ans, stu_ans, ans.format(score, stu_ans, corr_ans))

    def test_winners(self):
        generate_intel('data.txt', True)
        ans = _("For the given students' achievements {} you decided {} won but {} clearly did.")
        stu_ans = houseCup.winning_house('data.txt')
        corr_ans = corr.winning_house('data.txt')
        with open('data.txt', 'r') as f:
            score = f.readlines()
        self.assertEqual(corr_ans, stu_ans, ans.format(score, stu_ans, corr_ans))

    def test_IOError(self):
        self.assertRaises(IOError, houseCup.winning_house, 'IOError.txt')


if __name__ == '__main__':
    unittest.main()
