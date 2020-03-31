#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import ast

import CorrQ as corr
import q


ASKED_FUNCTION_NAMES = ['accumulate', 'sum', 'mul', 'max', 'concat']
FUNCTIONS = [(q.sum, 12), (q.mul, 48), (q.concat, '12423'), (q.max, 4)]
L = [1, 2, 4, 2, 3]

def sub(a, b):
    return a - b
    

class TestAcc(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'accumulate') and hasattr(q, 'sum') and hasattr(q, 'mul') and hasattr(q, 'max') and hasattr(q, 'concat'), _("You did not name the method as expected."))

    def test_basic_case(self):
        ans = _("L'utilisation de votre fonction {} a renvoyé un résultat inattendu.")
        for f in FUNCTIONS:
            stu_ans = f[0](L)
            self.assertEqual(f[1], stu_ans, ans.format(f[0].__name__))

    def test_other_function(self):
        a = [100, 54, 23, 12, 1]
        ans = _("Votre fonction accumulate ne semble pas fonctionner quand on lui donne d'autre fonctions.")
        stu_ans = q.accumulate(200, sub, a)
        self.assertEqual(10, stu_ans, ans)

    def test_call(self):
        with open("q.py", "r") as f:
            tree = ast.walk(ast.parse(f.read()))
            functions = [f for f in tree if isinstance(f, ast.FunctionDef)]
            functions_names = [f.name for f in functions]
        asked_functions = filter(lambda x: x.name in ASKED_FUNCTION_NAMES, functions)
        for f in asked_functions:
            if f.name != "accumulate" and not [x for x in ast.walk(f) if isinstance(x, ast.Call) and getattr(x.func, 'id', None) == "accumulate"]:
                self.fail(_("La fonction: {} ne fait pas appel à la fonction accumulate".format(f.name)))
             


if __name__ == '__main__':
    unittest.main()
