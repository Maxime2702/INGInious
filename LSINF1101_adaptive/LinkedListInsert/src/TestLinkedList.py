#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import copy

import CorrLinkedList as corr
import linkedlist


class TestList(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(linkedlist.LinkedList, 'insert'), "Vous n'avez pas fourni la fonction ``insert`` demandée pour la classe LinkedList")
        
    def test_empty(self):
        ans = "En utilisant insert sur une LinkedList vide, l'élément deviendra head de la LinkedList."
        stu_ans = linkedlist.LinkedList([])
        stu_ans.insert(2)
        self.assertEqual(linkedlist.LinkedList([2]), stu_ans, ans)

    def test_lst(self):
        ans = "La méthode insert ne semble pas fonctionner correctement"
        lst = [random.randint(1, 10) for _ in range(random.randint(3, 5))]
        lst.sort()
        corr_ans = corr.LinkedList(copy.deepcopy(lst))
        stu_ans = linkedlist.LinkedList(lst)
        stu_ans.insert(5)
        corr_ans.insert(5)
        self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
