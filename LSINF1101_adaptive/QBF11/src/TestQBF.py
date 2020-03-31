#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import string

import CorrQBF as corr
import qbf


class TestQBF(unittest.TestCase):
    def setUp(self):
        self.emptycirclist = qbf.CircularLinkedList()
        self.oneelementlist = qbf.CircularLinkedList()
        self.oneelementlist.add("Kim")
        self.twoelementlist = qbf.CircularLinkedList()
        self.twoelementlist.add("Charles")
        self.twoelementlist.add("Siegfried")
        self.threeelementlist = qbf.CircularLinkedList()
        self.threeelementlist.add("Charles")
        self.threeelementlist.add("Siegfried")
        self.threeelementlist.add("Charles")
    
    def test_exist(self):
        self.assertTrue((hasattr(qbf.CircularLinkedList, 'remove') and hasattr(qbf.CircularLinkedList, 'removeAll')), "Vous n'avez pas fourni la les méthodes remove ou removeAll.")

    def test_remove_fromempty(self):
        self.emptycirclist.remove("Kim")
        ans = "Une suppression dans une liste vide ne devrait pas la modifier."
        self.assertIsNone(self.emptycirclist.first(), ans)
        self.assertIsNone(self.emptycirclist.last(), ans)

    def test_remove_fromsingletonlist_1(self):
        # removing only element from singleton list produces empty list
        self.oneelementlist.remove("Kim")
        ans = "Une suppression dans une liste avec un élément devrait remettre first et last à None."
        self.assertIsNone(self.oneelementlist.first(), ans)
        self.assertIsNone(self.oneelementlist.last(), ans)

    def test_remove_fromsingletonlist_2(self):
        # removing non-existing element from singleton list leaves list intact
        self.oneelementlist.remove("Foo")
        ans = "Une suppression d'un élément inexistant dans une liste ne devrait pas altérer la liste."
        self.assertEqual(self.oneelementlist.first().value(),"Kim", ans)
        self.assertEqual(self.oneelementlist.last().value(),"Kim", ans)
        self.assertEqual(self.oneelementlist.first(),self.oneelementlist.last(), ans)
        self.assertEqual(self.oneelementlist.first(),self.oneelementlist.first().next(), ans)
        self.assertEqual(self.oneelementlist.last(),self.oneelementlist.last().next(), ans)
        self.assertEqual(self.oneelementlist.first().next(),self.oneelementlist.last(), ans)
        self.assertEqual(self.oneelementlist.last().next(),self.oneelementlist.first(), ans)

    def test_remove_1(self):
        # removing first element from a two-element lits produces one-element list
        self.twoelementlist.remove("Siegfried")
        ans = "La suppression d'un élément commençant une liste doit modifier first."
        self.assertEqual(self.twoelementlist.first().value(),"Charles", ans)
        self.assertEqual(self.twoelementlist.last().value(),"Charles", ans)
        self.assertEqual(self.twoelementlist.first(),self.twoelementlist.last(), ans)

    def test_remove_2(self):
        # removing second element from a two-element lits produces one-element list
        self.twoelementlist.remove("Charles")
        ans = "La suppression d'un élément finissant une liste doit modifier last."
        self.assertEqual(self.twoelementlist.first().value(),"Siegfried", ans)
        self.assertEqual(self.twoelementlist.last().value(),"Siegfried", ans)
        self.assertEqual(self.twoelementlist.first(),self.twoelementlist.last(), ans)

    def test_remove_all(self):
        # removing two occurences of an element from a three-element lits produces one-element list
        self.threeelementlist.removeAll("Charles")
        ans = "RemoveAll est supposé supprimer l'ensemble des instances avec une même valeur et mettre à jours first et last le cas échéant."
        self.assertEqual(self.threeelementlist.first().value(),"Siegfried", ans)
        self.assertEqual(self.threeelementlist.last().value(),"Siegfried", ans)
        self.assertEqual(self.threeelementlist.first(),self.threeelementlist.last(), ans)





if __name__ == '__main__':
    unittest.main()
