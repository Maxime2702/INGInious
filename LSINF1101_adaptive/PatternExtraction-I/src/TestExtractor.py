#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrExtractor as corr
import extractor


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


def generate_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))


def strip_trailing_space(s):
    if len(s) > 0 and s[-1] == ' ': return s[:-1]
    return s


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(extractor, 'extract'), _("You did not name the method as expected."))

    def test_extract(self):
        a = [generate_code() for _ in range(5)]
        ans = _("The natures of {} is {} and you returned {}.")
        for e in a:
            stu_ans = extractor.extract(e)
            corr_ans = corr.extract(e)
            self.assertEqual(equal_string(corr_ans), equal_string(strip_trailing_space(stu_ans)), ans.format(e, corr_ans, stu_ans))

    def test_char_y(self):
        a = 'y' + generate_code()
        ans = _("N'avez-vous pas mal attribué certains caractères? Pour {} vous avez renvoyé {}.")
        stu_ans = extractor.extract(a)
        corr_ans = corr.extract(a)
        self.assertEqual(equal_string(corr_ans), equal_string(strip_trailing_space(stu_ans)), ans.format(a, stu_ans))

    def test_upper(self):
        a = generate_code().upper()
        ans = _("Traitez-vous les majuscules? Pour {} vous avez renvoyé {}.")
        stu_ans = extractor.extract(a)
        corr_ans = corr.extract(a)
        self.assertEqual(equal_string(corr_ans), equal_string(strip_trailing_space(stu_ans)), ans.format(a, stu_ans))

    def test_lower(self):
        a = generate_code().lower()
        ans = _("Traitez-vous les minuscules? Pour {} vous avez renvoyé {}.")
        stu_ans = extractor.extract(a)
        corr_ans = corr.extract(a)
        self.assertEqual(equal_string(corr_ans), equal_string(strip_trailing_space(stu_ans)), ans.format(a, stu_ans))


if __name__ == '__main__':
    unittest.main()
