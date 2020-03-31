#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrAdmission as corr
import admission


letter = _("HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY \n Headmaster : Albus Dumbledore \n (Order of Merlin, First "
           "Class, Grand Sorc., Chf. Warlock, Supreme Mugwump, International Confed. of Wizards) \n\n Dear Mr/Ms. #, "
           "\n\n We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and "
           "Wizardry. Please find enclosed a list of all necessary books and equipment. \n\n Term begins on 1 "
           "September. We await your owl by no later than 31 July. \n\n Yours sincerely, \n\n "
           "Minerva McGonagall \n Deputy Headmistress \n")

def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


def generate_intel(file):
    with open(file, 'w+') as f:
        f.write(letter)


class TestAdmission(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(admission, 'write'), _("You did not name the method as expected."))

    def test_write(self):
        filename = 'letter.txt'
        name = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        ans = _("The letter expected of the given file was {} and you returned {}.")

        generate_intel(filename)
        file = admission.write(filename, name)

        with open(filename, 'r') as f:
            stu_ans = f.read(file)
        corr_ans = letter.replace('#', name)
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))

    def test_IOError(self):
        self.assertRaises(IOError, admission.write, 'IOError.txt', 'toto')
        #try except with self.fail()


if __name__ == '__main__':
    unittest.main()
