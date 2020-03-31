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

import CorrM10 as corr
import mission10


class TestM10(unittest.TestCase):
    def test_exist_class(self):
        for cls in ['Article', 'ArticleReparation', 'Facture', 'Piece', 'ArticlePiece']:
            self.assertTrue(hasattr(mission10, cls), "Vous n'avez pas créé la classe {} comme demandé.".format(cls))
                   
    def test_exist_func_piece(self):
        for fun in ['__init__', 'description', 'prix', 'poids', 'fragile', 'tva_reduit', '__eq__']:
            self.assertTrue(hasattr(mission10.Piece, fun), "Vous n'avez pas créé la fonction {} de la classe Piece comme demandé.".format(fun))

    def test_extends_piece(self):
        article = mission10.ArticlePiece(10, 10)
        self.assertTrue(isinstance(article, mission10.Article), "ArticlePiece n'hérite pas de la classe Article.")  

    def test_extends_repair(self):
        article = mission10.ArticleReparation(10)
        self.assertTrue(isinstance(article, mission10.Article), "ArticleReparation n'hérite pas de la classe Article.")  
            
    def test_eq(self):
        ans = "La méthode testant l'égalité de deux instances de Piece ne renvoit le résultat attendu. Comparez-vous les bons attributs?"
        self.assertTrue(mission10.Piece("test", 10.0, 10.0, True, True) == mission10.Piece("test", 10.0, 10.0, True, True), ans)
        self.assertTrue(mission10.Piece("test", 10.0, 10.0, True, True) == mission10.Piece("test", 10.0, 10.0, False, True), ans)
        self.assertTrue(mission10.Piece("test", 10.0, 10.0, True, True) == mission10.Piece("test", 10.0, 10.0, True, False), ans)
        self.assertTrue(mission10.Piece("test", 10.0, 10.0, True, True) == mission10.Piece("test", 10.0, 11.0, True, True), ans)
        self.assertFalse(mission10.Piece("test", 10.0, 10.0, True, True) == mission10.Piece("test", 11.0, 10.0, True, True), ans)
        self.assertFalse(mission10.Piece("test", 10.0, 10.0, True, True) == mission10.Piece("teste", 10.0, 10.0, True, True), ans)
        

if __name__ == '__main__':
    unittest.main()

