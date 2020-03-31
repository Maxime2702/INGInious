#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import subprocess
import unittest
import random
import shlex
import sys
from contextlib import redirect_stdout
import io

import CorrM09 as corr
import mission9


class TestM09(unittest.TestCase):
    def test_exist_class(self):
        for cls in ['Duree', 'Chanson', 'Album']:
            self.assertTrue(hasattr(mission9, cls), "Vous n'avez pas créé la classe {} comme demandé.".format(cls))
            
            
    def test_exist_func_duree(self):
        for fun in ['__init__', 'ajouter', 'toSecondes', 'delta', 'apres', '__str__']:
            self.assertTrue(hasattr(mission9.Duree, fun), "Vous n'avez pas créé la fonction {} de la classe Duree comme demandé.".format(fun))

            
    def test_exist_func_chanson(self):
        for fun in ['__init__', '__str__']:
            self.assertTrue(hasattr(mission9.Chanson, fun), "Vous n'avez pas créé la fonction {} de la classe Chanson comme demandé.".format(fun))

            
    def test_exist_func_album(self):
        for fun in ['__init__', 'add']:
            self.assertTrue(hasattr(mission9.Album, fun), "Vous n'avez pas créé la fonction {} de la classe Album comme demandé.".format(fun))
            
    def test_duree_tos(self):
        h, m, s = 0, 3, 20
        stu_duree = mission9.Duree(h, m, s)
        self.assertEqual(200, stu_duree.toSecondes(), "La méthode toSeconds de votre classe Duree ne renvoit pas le nombre attendu.")
            
    def test_duree_delta(self):
        h1, m1, s1 = 0, 3, 20
        h2, m2, s2 = 0, 3, 15
        stu_duree1 = mission9.Duree(h1, m1, s1)
        stu_duree2 = mission9.Duree(h2, m2, s2)
        if stu_duree2.delta(stu_duree1) >= 0:
            self.fail("Votre méthode delta doit renvoyer un nombre négatif quand le temps de base est plus petit que le temps auquel il est comparé.")
        self.assertEqual(5, stu_duree1.delta(stu_duree2), "La méthode delta de votre classe Duree ne renvoit pas le nombre attendu.")
            
    def test_duree_ajouter(self):
        h, m, s = 0, 3, 20
        stu_duree = mission9.Duree(h, m, s)
        stu_duree.ajouter(mission9.Duree(2, 57, 74))
        self.assertEqual("{:02}:{:02}:{:02}".format(3, 1, 34), str(stu_duree), "La méthode ajouter de votre classe Duree ne semble pas tenir compte du fait qu'il y a un nombre limité de secondes et de minutes possible.")
            
    def test_duree_apres(self):
        h1, m1, s1 = 0, 3, 20
        h2, m2, s2 = 0, 3, 15
        stu_duree1 = mission9.Duree(h1, m1, s1)
        stu_duree2 = mission9.Duree(h2, m2, s2)
        if stu_duree2.apres(stu_duree1):
            self.fail("Votre méthode apres devait renvoyer False pour les durées données mais a renvoyé True.")
        self.assertTrue(stu_duree1.apres(stu_duree2), "La méthode apres de votre classe Duree ne renvoit pas le booléen attendu (False au lieu de True).")
            
    def test_chanson_str(self):
        title, author, duration = "ceci est", "un test", corr.Duration(0, 3, 20)
        stu_song = mission9.Chanson(title, author, duration)
        self.assertEqual("{} - {} - {}".format(title, author, str(duration)), str(stu_song), "La méthode __str__ de votre classe Chanson ne renvoit pas le string attendu.")
       
            
    """ def test_result(self):
        ans = "Le résultat attendu était\n{}\nEt vous avez renvoyé:\n{}"
        with open('err.txt', 'w+', encoding="utf-8") as f:
            py_cmd = "python3 mission9.pyc"
            try:
                resproc = subprocess.Popen(shlex.split(py_cmd), universal_newlines=True, stderr=f, stdout=subprocess.PIPE)
                result, tanguy_et_francois = resproc.communicate()
                f.seek(0)
                error = f.read()
            except (IOError, BrokenPipeError):
                result = "Erreur lors de l'exécution du programme sur INGINious."
        if error != "":
            raise Exception(error)
        with io.StringIO() as out, redirect_stdout(out):
            corr.main()
            corr_ans = out.getvalue()
        if corr_ans != result:
            self.fail(ans.format(corr_ans, result))"""
        

if __name__ == '__main__':
    unittest.main()

