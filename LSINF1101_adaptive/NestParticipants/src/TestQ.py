#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

class TestNestedParticipants(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'nest_students'), _("You did not name the method as expected."))

    def test_empty(self):
        l = [("Jean", "LINFO1111"), ("Jean", "LINFO1101"), ("Pierre", "LINFO1101"), ("Pierre", "LINFO1112")]
        ans = _("Avec une liste de cours vide, vous trouvez tout de même des étudiants.")
        stu_ans = q.nest_students([])
        corr_ans = []
        self.assertEqual(corr_ans, stu_ans, ans)

    def test_in(self):
        l = [("Jean", "LINFO1111"), ("Jean", "LINFO1101"), ("Pierre", "LINFO1101"), ("Pierre", "LINFO1112")]
        ans = _("Pour les, {} sont isncrits et vous renvoyez: {}")
        stu_ans = q.nest_students(l)
        corr_ans = [('LINFO1101', ['Jean', 'Pierre']), ('LINFO1111', ['Jean']), ('LINFO1112', ['Pierre'])]
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()