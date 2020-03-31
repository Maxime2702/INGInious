#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrMorse as corr
import morse


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(morse, 'translate'), _("You did not name the method as expected."))

    def test_dic_use(self):
        a = 'A' + (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        ans = _("The representation of {} in Morse is {} and you returned {}. You did not use the given dictionary.")
        stu_ans = morse.translate(a)
        corr_ans = corr.translate(a)
        self.assertEqual(equal_string(corr_ans), equal_string(stu_ans), ans.format(a, corr_ans, stu_ans))

    def test_translation(self):
        a = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) for _ in range(5)]
        ans = _("The representation of {} in Morse is {} and you returned {}.")
        for e in a:
            stu_ans = morse.translate(e)
            corr_ans = corr.translate(e)
            self.assertEqual(equal_string(corr_ans), equal_string(stu_ans), ans.format(e, corr_ans, stu_ans))

    def test_oov(self):
        a = ['ç', '#', '~', '@', '$']
        ans = "{} aurait du lever une exception à cause de caractères spéciaux mais ne l'a pas fait."
        for e in a:
            flag = False
            try:
                stu_ans = morse.translate(e)
            except TypeError:
                flag = True
            self.assertTrue(flag, ans.format(e))


if __name__ == '__main__':
    unittest.main()
