#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import copy

import CorrLinkedList as corr
import linkedlist


class TestList(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(linkedlist.LinkedList, '__str__'), "Vous n'avez pas fourni la fonction ``__str__`` demandée pour la classe LinkedList")
        
    def test_empty(self):
        ans = "En utilisant __str__ sur une LinkedList vide, le string renvoyé devrait être '[ ]' et était {}."
        stu_ans = str(linkedlist.LinkedList([]))
        self.assertEqual('[ ]', stu_ans, ans.format(stu_ans)) 

    def test_lst(self):
        ans = "La méthode __str__ ne semble pas fonctionner correctement, le string renvoyé devrait être {} et était {}."
        ln = random.randint(3, 5)
        lst = [random.randint(1, 10) for _ in range(ln)]
        corr_ans = str(corr.LinkedList(copy.deepcopy(lst)))
        stu_ans = str(linkedlist.LinkedList(lst))
        self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
