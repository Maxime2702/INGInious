#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import ast

import CorrQ as corr
import q

class TestBinarySearch(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'binary_search'), _("You did not name the method as expected."))
        
    def test_no_for_loop(self):
        with open('q.py', 'r') as f:
            s = f.read()
            if [x for x in ast.walk(ast.parse(s)) if isinstance(x, ast.For)]:
                ans = _("Les boucles for ne sont pas autorisées.")
                self.fail(ans)

    def test_search(self):
        cours = {'LINFO1101': ['Jean', 'Pierre'], 'LINFO1111': ['Jean'], 'LINFO1110': ['Jean'], 'LINFO1112': ['Jacques', 'Pierre'], 'LINFO1113': ['Pierre']}
        l = [('LINFO1101', ['Jean', 'Pierre']), ('LINFO1110', ['Jean']), ('LINFO1111', ['Jean']), ('LINFO1112', ['Jacques', 'Pierre']), ('LINFO1113', ['Pierre'])]
        for c in cours.keys():
            ans = _("Pour le cours {} les isncrits sont {} et non {}")
            stu_ans = q.binary_search(c, l)
            corr_ans = cours[c]
            self.assertEqual(corr_ans, stu_ans, ans.format(c, corr_ans, stu_ans))

    def test_empty(self):
        c = 'LINFO1101'
        ans = _("Pour une liste de cours vide, votre algorithme a tout de même renvoyé autre chose qu'une liste d'étudiants vide.")
        stu_ans = q.binary_search(c, [])
        self.assertEqual([], stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
