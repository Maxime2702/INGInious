#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import copy

import CorrLinkedList as corr
import linkedlist


class TestList(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(linkedlist.LinkedList, '__init__'), "Vous n'avez pas fourni la fonction ``__init__`` demandée pour la classe LinkedList")
        
    def test_empty(self):
        ans = "En passant une liste vide au constructeur, une LinkedList devrait tout de même être créée."
        stu_ans = linkedlist.LinkedList([])
        self.assertEqual(corr.LinkedList([]), stu_ans, ans)

    def test_lst(self):
        random_list = [[random.randint(1, 3) for _ in range(random.randint(1, 3)) ] + [4] for _ in range(random.randint(1, 5))]
        ans = "Votre fonction n'ajoute pas correctement les éléments de la liste dans la LinkedList."
        for lst in random_list:
            corr_list = corr.LinkedList(copy.deepcopy(lst))
            stu_list = linkedlist.LinkedList(lst)
            self.assertEqual(corr_list, stu_list, ans)


if __name__ == '__main__':
    unittest.main()
