#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import string
import random
import unicodedata

import CorrEmploye as corr
import employe


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestEmploye(unittest.TestCase):
    def test_exist(self):
        self.assertTrue((hasattr(employe.Employe, '__init__') and hasattr(employe.Employe, '__str__') and hasattr(employe.Employe, 'augmente')),
                        _("Vous n'avez pas fourni les méthodes init ou str ou augmente."))

    def test_str(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        salary = [random.randint(1000, 3500) for _ in range(8)]
        ans = _("Avec les données: {}, {}, vous avez créé l'employé {} plutot que {}")
        stu_ans = employe.Employe(name, salary)
        corr_ans = corr.Employe(name, salary)
        self.assertEqual(equal_string(str(corr_ans)), equal_string(str(stu_ans)), ans.format(name, salary, stu_ans,
                                                                                             corr_ans))

    def test_augmente(self):
        e = employe.Employe('Eric', 100)
        p = 20
        e.augmente(p)
        ans = _("Avec les données: {}, {} et une augmentation de {}, vous avez un salaire de {}")
        self.assertEqual(e.salaire, 120, ans.format(e.nom, 100, p, e.salaire))

    def test_diminue(self):
        e = employe.Employe('Eric', 100)
        p = -20
        e.augmente(p)
        ans = _("Avec les données: {}, {} et une réduction de {}, vous avez un salaire de {}")
        self.assertEqual(e.salaire, 80, ans.format(e.nom, 100, p, e.salaire))


if __name__ == '__main__':
    unittest.main()
