#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import timeout_decorator

import CorrChildren as corr
import child


class TestChildren(unittest.TestCase):

    @timeout_decorator.timeout(1, exception_message=_("Be sure you stop once you are back to the first children.\n"
                                                      "You don't want to have more than you already have..."))
    def test_basic_loop(self):
        node1 = corr.Child()
        node2 = corr.Child()
        node3 = corr.Child()
        node1.next = node2  # 12->99
        node2.next = node3  # 99->37
        node3.next = node1
        self.assertEqual(True, child.is_every_child_here(node1),  msg=_("Well... You got it wrong, so try again.\n"
                                                                        "Are you blind? Everyone's there!"))

    @timeout_decorator.timeout(1, exception_message=_("Be sure you stop once you are back to the first children.\n"
                                                      "You don't want to have more than you already have..."))
    def test_broken_loop(self):
        node1 = corr.Child()
        node2 = corr.Child()
        node3 = corr.Child()
        node1.next = node2  # 12->99
        node2.next = node3  # 99->37
        self.assertEqual(False, child.is_every_child_here(node1),  msg=_("Well... You got it wrong, so try again.\n"
                                                                         "You actually lost a child"))

        
if __name__ == '__main__':
    unittest.main()
