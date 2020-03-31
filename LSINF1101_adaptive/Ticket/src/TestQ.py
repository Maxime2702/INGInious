#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestStudent(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q.Ticket, '__init__'), _("Vous n'avez pas implémenté la méthode __init__."))

    def test_multi_ticket(self):
        ans = "La {}ème instance créée de votre classe Ticket devrait avoir le numéro {} et a le numéro {}. Incrémentez-vous correctement la variable de classe?"
        for i in range(random.randint(1, 10)):
            stu_ans = q.Ticket()
            corr_ans = corr.Ticket()
        self.assertEqual(corr_ans.numero(), stu_ans.numero(), ans.format(i-1, corr_ans.numero(), stu_ans.numero()))

    def test_cls_var(self):
        for e in dir(q):
            if not e.endswith('__') and e != 'Ticket':
                self.fail("Vous utilisez une variable globale ce qui est déconseillé; essayez d’adapter votre exercice afin d’utiliser une variable de classe au lieu d’une variable globale")


if __name__ == '__main__':
    unittest.main()
