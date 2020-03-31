#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import string

import CorrQBF as corr
import qbf


class TestQBF(unittest.TestCase):
    
    def test_exist(self):
        self.assertTrue('moveforward' in qbf.MirrorRobot.__dict__ and 'movebackward' in qbf.MirrorRobot.__dict__ and 'turnleft' in qbf.MirrorRobot.__dict__ and 'turnright' in qbf.MirrorRobot.__dict__ and 'unplay' in qbf.MirrorRobot.__dict__, "Vous n'avez pas fourni une des méthodes à redéfinir de la classe MirrorRobot.")
        
    def setUp(self):
        self.corrRobot1 = corr.Robot("corrRobot1")
        self.corrRobot2 = corr.Robot("corrRobot2")
        self.mirrorbot1 = corr.MirrorRobot(self.corrRobot1, self.corrRobot2)
        
        self.studRobot1 = corr.Robot("studRobot1")
        self.studRobot2 = corr.Robot("studRobot2")
        self.mirrorbot2 = qbf.MirrorRobot(self.studRobot1, self.studRobot2)
        
    def test_moveforward(self):
        for _ in range(10):
            dist = random.randrange(1000)
            self.mirrorbot1.moveforward(dist)
            self.mirrorbot2.moveforward(dist)
            
            self.assertEqual(self.mirrorbot1.getHistory(), self.mirrorbot2.getHistory(), "Votre MirrorRobot n'enregistre pas correctement son historique pour la méthode moveforward.")
            self.assertEqual(self.corrRobot1.getHistory(), self.studRobot1.getHistory(), "Votre premier robot n'effectue pas les actions attendues pour la méthode moveforward.")
            self.assertEqual(self.corrRobot2.getHistory(), self.studRobot2.getHistory(), "Votre deuxième robot n'effectue pas les actions attendues pour la méthode moveforward.")
            
    def test_movebackward(self):
        for _ in range(10):
            dist = random.randrange(1000)
            self.mirrorbot1.movebackward(dist)
            self.mirrorbot2.movebackward(dist)
            
            self.assertEqual(self.mirrorbot1.getHistory(), self.mirrorbot2.getHistory(), "Votre MirrorRobot n'enregistre pas correctement son historique pour la méthode movebackward.")
            self.assertEqual(self.corrRobot1.getHistory(), self.studRobot1.getHistory(), "Votre premier robot n'effectue pas les actions attendues pour la méthode movebackward.")
            self.assertEqual(self.corrRobot2.getHistory(), self.studRobot2.getHistory(), "Votre deuxième robot n'effectue pas les actions attendues pour la méthode movebackward.")
            
    def test_turnleft(self):
        for _ in range(10):
            self.mirrorbot1.turnleft()
            self.mirrorbot2.turnleft()
            
            self.assertEqual(self.mirrorbot1.getHistory(), self.mirrorbot2.getHistory(), "Votre MirrorRobot n'enregistre pas correctement son historique pour la méthode turnleft.")
            self.assertEqual(self.corrRobot1.getHistory(), self.studRobot1.getHistory(), "Votre premier robot n'effectue pas les actions attendues pour la méthode turnleft.")
            self.assertEqual(self.corrRobot2.getHistory(), self.studRobot2.getHistory(), "Votre deuxième robot n'effectue pas les actions attendues pour la méthode turnleft.")
            
    def test_turnright(self):
        for _ in range(10):
            self.mirrorbot1.turnright()
            self.mirrorbot2.turnright()
            
            self.assertEqual(self.mirrorbot1.getHistory(), self.mirrorbot2.getHistory(), "Votre MirrorRobot n'enregistre pas correctement son historique pour la méthode turnright.")
            self.assertEqual(self.corrRobot1.getHistory(), self.studRobot1.getHistory(), "Votre premier robot n'effectue pas les actions attendues pour la méthode turnright.")
            self.assertEqual(self.corrRobot2.getHistory(), self.studRobot2.getHistory(), "Votre deuxième robot n'effectue pas les actions attendues pour la méthode turnright.")
   
    def test_random_moves(self):
        for _ in range(40):
            dist = random.randrange(1000)
            action = random.choice(["up", "down", "left", "right"])
            if action == "up":
                self.mirrorbot1.moveforward(dist)
                self.mirrorbot2.moveforward(dist)
            if action == "down":
                self.mirrorbot1.movebackward(dist)
                self.mirrorbot2.movebackward(dist)
            if action == "left":
                self.mirrorbot1.turnleft()
                self.mirrorbot2.turnleft()
            if action == "left":
                self.mirrorbot1.turnright()
                self.mirrorbot2.turnright()
                
            self.assertEqual(self.mirrorbot1.getHistory(), self.mirrorbot2.getHistory(), "Votre MirrorRobot n'enregistre pas correctement son historique.")
            self.assertEqual(self.corrRobot1.getHistory(), self.studRobot1.getHistory(), "Votre premier robot n'effectue pas les actions attendues.")
            self.assertEqual(self.corrRobot2.getHistory(), self.studRobot2.getHistory(), "Votre deuxième robot n'effectue pas les actions attendues.")
            
        self.mirrorbot1.unplay()
        self.mirrorbot2.unplay()
        
        self.assertEqual(self.mirrorbot1.getHistory(), self.mirrorbot2.getHistory(), "Votre MirrorRobot n'efface pas son historique correctement.")
        self.assertEqual(self.corrRobot1.getHistory(), self.studRobot1.getHistory(), "Votre premier robot n'efface pas son historique correctement.")
        self.assertEqual(self.corrRobot2.getHistory(), self.studRobot2.getHistory(), "Votre deuxième robot n'efface pas son historique correctement.")


if __name__ == '__main__':
    unittest.main()
