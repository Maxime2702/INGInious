#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import string

import CorrLinkedList as corr
import linkedlist


class TestList(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(linkedlist, 'LinkedList'), _("You did not provide the LinkedList class"))
        self.assertTrue(hasattr(linkedlist.LinkedList, 'add') and hasattr(linkedlist.LinkedList, 'get_reverse'),
                        _("You did not provide the required methods"))
        self.assertTrue(hasattr(linkedlist, 'Node'), _("You did not provide the Node class"))
        self.assertTrue(hasattr(linkedlist.Node, 'get_next') and hasattr(linkedlist.Node, 'get_value'),
                        _("You did not provide the required methods in the Node class"))
        
    def test_empty(self):
        a = ""
        ans = _("When adding nothing get_reverse is supposed to return an empty string and you returned {}. \n You "
                "should watch you behaviour in case of empty lists.")
        for i in range(len(a)):
            stu_list = linkedlist.LinkedList()
            stu_ans = stu_list.get_reverse()
            corr_list = corr.LinkedList()
            corr_ans = corr_list.get_reverse()
            self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans))

    def test_reverse(self):
        random_list = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 10))
                               )for _ in range(random.randint(1, 10))]
        ans = _("The answer should be {} and you returned {}.")
        stu_list = linkedlist.LinkedList()
        corr_list = corr.LinkedList()
        for e in random_list:
            stu_list.add(e)
            corr_list.add(e)
            corr_ans = corr_list.get_reverse().replace(" ", "")
            stu_ans = stu_list.get_reverse().replace(" ", "")
            self.assertEqual(corr_ans, stu_ans, ans.format(corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
