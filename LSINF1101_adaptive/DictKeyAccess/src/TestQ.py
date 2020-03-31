#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

CITIES = [{"City": "Bruxelles", "Country": "Belgium"}, {"City": "Berlin", "Country": "Germany"}, {"City": "Paris", "Country": "France"}]

CORRECT = ('Berlin', 'Germany', "Votre programme ne semble pas trouver le pays associé à une ville.")
CORRECT_OOV = ('Londres', False,"Votre programme ne renvoit pas False dans le cas où la ville n'est pas enregistrée.")


TESTS = [CORRECT, CORRECT_OOV]


class TestGetCountry(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'get_country'), _("You did not name the method as expected."))

    def test_cases(self):
        for t in TESTS:
            ans = t[2]
            corr_ans = t[1]
            stu_ans = q.get_country(CITIES, t[0])
            self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
