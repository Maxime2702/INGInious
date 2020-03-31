#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import ast

import CorrEq as corr
import eq

ASKED_FUNCTION_NAMES = ["rho", "solution", "n_solutions"]


class TestEq(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        with open("eq.py", "r") as f:
            super().__init__(*args, **kwargs)
            self.tree = ast.walk(ast.parse(f.read()))
            self.functions = [f for f in self.tree if isinstance(f, ast.FunctionDef)]
            self.functions_names = [f.name for f in self.functions]
            self.no_sol_tuples = (1, 1, 1), (1, 2, 3), (-6, 2, -15), (-25, 10, -100), (25, 10, 2)
            self.one_sol_tuples = (2, 0, 0), (25, 0, 0), (4, 4, 1),  (4, 8, 4)
            self.two_sol_tuples = (1, 1, -1), (-1, 2, 3), (-6, 2, 15), (-25, 10, 100), (25, 10, -2), (2, 100, 3)
        
        
    def test_implements_functions(self):
        missing_functions = list(filter(lambda x: x not in self.functions_names, ASKED_FUNCTION_NAMES))
        if missing_functions:
            self.fail(_("Vous n'avez pas correctement défini les fonctions suivantes: {}".format(", ".join(missing_functions))))

    def test_call_to_rho(self):
        asked_functions = filter(lambda x: x.name in ASKED_FUNCTION_NAMES, self.functions)
        for f in asked_functions:
            # for each function different from rho, check if they call rho directly
            if f.name != "rho" and not [x for x in ast.walk(f) if isinstance(x, ast.Call) and getattr(x.func, 'id', None) == "rho"]:
                self.fail(_("La fonction: {} ne fait pas appel à la fonction rho".format(f.name)))
             
                
    def test_rho(self):
        ans = _("L'équation définie par le triplet {} a un rho de {}, mais la fonction  rho a retourné {}.")
        for t in self.no_sol_tuples + self.one_sol_tuples + self.two_sol_tuples: 
            stu_ans = eq.rho(*t)
            corr_ans = corr.rho(*t)
            self.assertEqual(corr_ans, stu_ans, ans.format(t, corr_ans, stu_ans))
                 
    def test_no_solution(self):
        ans = _("L'équation définie par le triplet {} n'a aucune solution, mais la fonction n_solutions a retourné {}.")
        for t in self.no_sol_tuples: 
            stu_ans = eq.n_solutions(*t)
            self.assertEqual(0, stu_ans, ans.format(t, stu_ans))
                               
    def test_one_solution(self):
        for t in self.one_sol_tuples: 
            ans = _("L'équation définie par le triplet {} a strictement une solution, mais la fonction n_solutions a retourné {}.")
            stu_ans = eq.n_solutions(*t)
            self.assertEqual(1, stu_ans, ans.format(t, stu_ans))
                               
    def test_two_solutions(self):
        for t in self.two_sol_tuples: 
            ans = _("L'équation définie par le triplet {} a deux solutions, mais la fonction n_solutions a retourné {}.")
            stu_ans = eq.n_solutions(*t)
            self.assertEqual(2, stu_ans, ans.format(t, stu_ans))
                               
    def test_find_the_one_solution(self):
        for t in self.one_sol_tuples: 
            ans = _("L'équation définie par le triplet {} a la solution {}, mais la fonction solution a retourné {}.")
            stu_ans = eq.solution(*t)
            corr_ans = corr.solution(*t)
            self.assertAlmostEqual(corr_ans, stu_ans, places=7, msg=ans.format(t, corr_ans, stu_ans))    
            
    def test_find_the_min_solution(self):
        for t in self.two_sol_tuples: 
            ans = _("L'équation définie par le triplet {} a la solution minimale {}, mais la fonction solution a retourné {}.")
            stu_ans = eq.solution(*t)
            corr_ans = corr.solution(*t)
            self.assertAlmostEqual(corr_ans, stu_ans, places=7, msg=ans.format(t, corr_ans, stu_ans))                         
      
if __name__ == '__main__':
    unittest.main()
