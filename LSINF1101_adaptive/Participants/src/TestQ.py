#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestParticipants(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'students'), _("You did not name the method as expected."))

    def test_empty(self):
        l = [("Jean", "LINFO1111"), ("Jean", "LINFO1101"), ("Pierre", "LINFO1101"), ("Pierre", "LINFO1112")]
        ans = _("Avec une liste de cours vide, vous trouvez tout de même un étudiant.")
        stu_ans = q.students("LINFO1101", [])
        corr_ans = []
        self.assertEqual(corr_ans, stu_ans, ans)

    def test_in(self):
        l = [("Jean", "LINFO1111"), ("Jean", "LINFO1101"), ("Pierre", "LINFO1101"), ("Pierre", "LINFO1112")]
        ans = _("Pour le cours de LINFO1101, {} sont isncrits et vous renvoyez: {}")
        stu_ans = q.students("LINFO1101", l)
        corr_ans = ["Jean", "Pierre"]
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))

    def test_not_in(self):
        l = [("Jean", "LINFO1111"), ("Jean", "LINFO1101"), ("Pierre", "LINFO1101"), ("Pierre", "LINFO1112")]
        ans = _("Avec un cours inexistant, vous trouvez tout de même un étudiant.")
        stu_ans = q.students("", l)
        corr_ans = []
        self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
