#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import ast

import CorrEq as corr
import eq

ASKED_FUNCTION_NAMES = ["solveur"]


class TestEq(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        with open("eq.py", "r") as f:
            super().__init__(*args, **kwargs)
            self.tree = ast.walk(ast.parse(f.read()))
            self.functions = [f for f in self.tree if isinstance(f, ast.FunctionDef)]
            self.functions_names = [f.name for f in self.functions]
            self.no_sol_tuples = [[1, 1, 1], [1, 2, 3], [-6, 2, -15], [-25, 10, -100], [25, 10, 2]]
            self.one_sol_tuples = [[2, 0, 0], [25, 0, 0], [4, 4, 1],  [4, 8, 4]]
            self.two_sol_tuples = [[1, 1, -1], [-1, 2, 3], [-6, 2, 15], [-25, 10, 100], [25, 10, -2], [2, 100, 3]]
        
        
    def test_implements_functions(self):
        missing_functions = list(filter(lambda x: x not in self.functions_names, ASKED_FUNCTION_NAMES))
        if missing_functions:
            self.fail(_("Vous n'avez pas correctement défini les fonctions suivantes: {}".format(", ".join(missing_functions))))

    #def test_call_to_listcomp(self):
    #    asked_functions = filter(lambda x: x.name in ASKED_FUNCTION_NAMES, self.functions)
    #    for f in asked_functions:
    #        # for each function different from rho, check if they call rho directly
    #        if not [x for x in ast.walk(f) if isinstance(x, ast.ListComp)]:
    #            self.fail(_("La fonction: {} n'utilise pas de list comprehension".format(f.name)))
             
    def test_empty_list(self):
        ans = _("Quand l'input est une liste vide, la fonction solveur devrait retourner une liste vide, mais a retourné {}.")
        stu_ans = eq.solveur([])
        self.assertEqual([], stu_ans, ans.format(stu_ans))
                               
    def test_many_solutions(self):
        import random
        inpt = self.no_sol_tuples + self.one_sol_tuples + self.two_sol_tuples
        random.shuffle(inpt)
        ans = _("La/les solution(s) pour l'équation {} (située à l'indice {}) devrait être {}. Votre solution a cependant donné la solution {}.")
        stu_ans = eq.solveur(inpt)
        corr_ans = corr.solveur(inpt)
        if len(stu_ans) != len(corr_ans):
            self.fail("La fonction solveur ne retourne pas une liste avec un élément par équation.")
        for i, sol in enumerate(corr_ans):
            if len(sol) != len(stu_ans[i]):
                self.fail(ans.format(inpt[i], i, sol, stu_ans[i]))
            for j, sj in enumerate(sol):
                self.assertAlmostEqual(sj, stu_ans[i][j], places=7, msg=ans.format(inpt[i], i, sol, stu_ans[i]))
             
      
if __name__ == '__main__':
    unittest.main()
