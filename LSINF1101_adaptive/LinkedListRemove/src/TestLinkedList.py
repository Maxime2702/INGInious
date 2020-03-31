#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrLinkedList as corr
import linkedlist


class TestList(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(linkedlist.LinkedList, 'remove'), "Vous n'avez pas fourni la fonction ``remove`` demandée pour la classe LinkedList")
        
    def test_empty(self):
        ans = "En utilisant remove sur une LinkedList vide, la taille devrait rester à 0."
        stu_ans = linkedlist.LinkedList([])
        stu_ans.remove()
        self.assertEqual(0, stu_ans.size(), ans)

    def test_lst(self):
        ans = "La méthode remove ne semble pas fonctionner correctement"
        lst = [random.randint(1, 10) for _ in range(random.randint(3, 5))]
        corr_ans = corr.LinkedList(lst[1:])
        stu_ans = linkedlist.LinkedList(lst)
        stu_ans.remove()
        self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
