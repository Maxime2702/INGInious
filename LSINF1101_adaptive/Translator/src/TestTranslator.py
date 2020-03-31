#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrTranslator as corr
import translator


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(translator, 'translate'), _("You did not name the method as expected."))

    def test_translation(self):
        a = ["I shot an elephant in my pajama", "This is a test"]
        ans = _("The expected translation of {} in {} is {} and you returned {}.")
        for e in a:
            for lan in [translator.es, translator.fr]:
                stu_ans = translator.translate(e, lan)
                corr_ans = corr.translate(e, lan)
                self.assertEqual(equal_string(corr_ans.lower()), equal_string(stu_ans.lower()), ans.format(e, lan, corr_ans, stu_ans))

    def test_oov(self):
        a = ["This is a shame", "I look like an elephant in my pajama"]
        ans = _("The expected translation of {} in {} is {} and you returned {}.")
        for e in a:
            for lan in [translator.es, translator.fr]:
                stu_ans = translator.translate(e, lan)
                corr_ans = corr.translate(e, lan)
                self.assertEqual(equal_string(corr_ans.lower()), equal_string(stu_ans.lower()), ans.format(e, lan, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
