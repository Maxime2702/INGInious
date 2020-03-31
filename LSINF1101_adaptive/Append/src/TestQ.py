#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestAppend(unittest.TestCase):
    def test_empty(self):
        stu_ans = q.app([])
        corr_ans = [("Jacques", "LINFO1112")]
        ans = _("Votre programme ne semble pas fonctionner pour des listes vides.")
        self.assertEqual(corr_ans, stu_ans, ans)
        
    def test_already_in(self):
        stu_ans = q.app([("Jacques", "LINFO1112")])
        corr_ans = [("Jacques", "LINFO1112"), ("Jacques", "LINFO1112")]
        ans = _("Votre programme ne semble pas fonctionner pour des listes ayant déjà cette entrée.")
        self.assertEqual(corr_ans, stu_ans, ans)

    def test_filled(self):
        l = [("Jean", "LINFO1111"), ("Jean", "LINFO1101"), ("Pierre", "LINFO1101"), ("Pierre", "LINFO1112")]
        ans = _("Votre programme ne semble pas fonctionner, voici la liste attendue: {} \n Et voici la votre: {}.")
        stu_ans = q.app(l[:])
        corr_ans = l + [("Jacques", "LINFO1112")]
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
