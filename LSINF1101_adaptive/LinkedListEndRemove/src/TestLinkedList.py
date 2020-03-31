#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrLinkedList as corr
import linkedlist


class TestList(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(linkedlist.LinkedList, 'remove_from_end'), "Vous n'avez pas fourni la fonction ``remove_from_end`` demandée pour la classe LinkedList")
        
    def test_empty(self):
        ans = "En utilisant remove sur une LinkedList vide, la taille devrait rester à 0."
        stu_ans = linkedlist.LinkedList([])
        stu_ans.remove_from_end()
        self.assertEqual(linkedlist.LinkedList([]), stu_ans, ans)
        self.assertEqual(0, stu_ans.size(), ans)    
        
    def test_one(self):
        ans = "En utilisant remove sur une LinkedList avec un seul élément, la liste devrait être vide."
        stu_ans = linkedlist.LinkedList([2])
        stu_ans.remove_from_end()
        self.assertEqual(linkedlist.LinkedList([]), stu_ans, ans)
        self.assertEqual(0, stu_ans.size(), ans + " Décrémentez-vous bien length?")    

    def test_lst(self):
        ans = "La méthode remove ne semble pas fonctionner correctement."
        ln = random.randint(3, 5)
        lst = [random.randint(1, 10) for _ in range(ln)]
        corr_ans = corr.LinkedList(lst[:-1])
        stu_ans = linkedlist.LinkedList(lst)
        stu_ans.remove_from_end()
        self.assertEqual(corr_ans, stu_ans, ans)
        self.assertEqual(ln-1, stu_ans.size(),  ans + " Décrémentez-vous bien length?")


if __name__ == '__main__':
    unittest.main()
