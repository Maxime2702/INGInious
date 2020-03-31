#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import timeout_decorator
import random
import string

import CorrTape as corr
import node
import tape


class TestDoubleLink(unittest.TestCase):
    
    def attr_node(self):
        ans = _("@1@: The Node class does not have the method {}")
        my_node = node.Node()
        self.assertTrue(has_attribute(my_node,"__init__"), ans.format("__init__"))
        self.assertTrue(has_attribute(my_node,"get_text"), ans.format("get_text"))
        self.assertTrue(has_attribute(my_node,"set_text"), ans.format("set_text"))

    def attr_tape(self):
        ans = _("@2@: The Tape class does not have the method {}")
        my_tape = tape.Tape()
        self.assertTrue(has_attribute(my_tape,"__init__"), ans.format("__init__"))
        self.assertTrue(has_attribute(my_tape,"next"), ans.format("next"))
        self.assertTrue(has_attribute(my_tape,"previous"), ans.format("previous"))
        self.assertTrue(has_attribute(my_tape,"get_length"), ans.format("get_length"))
        self.assertTrue(has_attribute(my_tape,"add"), ans.format("add"))
        self.assertTrue(has_attribute(my_tape,"write"), ans.format("write"))
        self.assertTrue(has_attribute(my_tape,"read"), ans.format("read"))
    
    def test_node(self):
        ans = _("@1@: node.get_text() give {} and it should give {}")
        s1 = new_string(10)
        my_node = node.Node(s1)
        self.assertEqual(s1, my_node.get_text(), ans.format(my_node.get_text(), s1))
        s2 = new_string(10)
        my_node.set_text(s2)
        self.assertEqual(s2, my_node.get_text(), ans.format(my_node.get_text(), s2))
        

    @timeout_decorator.timeout(1, exception_message=_("Be sure you don't have any infinite loop."))
    def test_tape_init(self):
        ans = _("@2@: Method init or read doesn\'t work. read() has given {} and it should have returned {}")
        s1 = new_string(10)
        my_tape = tape.Tape()
        my_tape.add(s1)
        self.assertEqual(s1, my_tape.read(), ans.format(my_tape.read(), s1))
        
    def test_tape_add(self):
        ans = _("@2@: La méthode add ne fonctionne pas. Le noeud sous le pointeur est: {} au lieu de {}.")
        s1 = new_string(10)
        s2 = new_string(10)
        my_tape = tape.Tape()
        my_tape.add(s1)
        self.assertEqual(s1, my_tape.read(), ans.format(my_tape.read(), s1) + '\nAprès 1 insertion.')
        my_tape.add(s2)
        self.assertEqual(s1, my_tape.read(), ans.format(my_tape.read(), s1) + '\nAprès 2 insertions.')
        
    def test_tape_next(self):
        ans = _("@2@: La méthode next ne fonctionne pas. Le noeud sous le pointeur est: {} au lieu de {}.")
        s1 = new_string(10)
        s2 = new_string(10)
        s3 = new_string(10)
        my_tape = tape.Tape()
        my_tape.add(s1)
        my_tape.add(s2)
        my_tape.add(s3)
        self.assertEqual(s2, my_tape.next(), ans.format(my_tape.read(), s2))
        self.assertEqual(s3, my_tape.next(), ans.format(my_tape.read(), s3))
        
        
    def test_tape_previous(self):
        ans = _("@2@: La méthode previous ne fonctionne pas. Le noeud sous le pointeur est: {} au lieu de {}.")
        s1 = new_string(10)
        s2 = new_string(10)
        s3 = new_string(10)
        my_tape = tape.Tape()
        my_tape.add(s1)
        my_tape.add(s2)
        my_tape.add(s3)
        x = my_tape.next()
        x = my_tape.next()
        self.assertEqual(s2, my_tape.previous(), ans.format(my_tape.read(), s2))
        self.assertEqual(s1, my_tape.previous(), ans.format(my_tape.read(), s3))
        
    def test_tape_length(self):
        ans = _("@2@: Method length doesn\'t give the good answer. It gives {} and it should give {}")
        my_tape = tape.Tape()
        for i in range(100):
            s1 = new_string(10)
            k = my_tape.get_length()
            self.assertEqual(i, k, ans.format(k, i))
            my_tape.add(s1)
        
    def test_tape_write_read(self):
        ans = _("@2@: Method write/read doesn\'t work. read() gives {} and it should give {}")
        s1 = new_string(10)
        s2 = new_string(10)
        s3 = new_string(10)
        my_tape = tape.Tape()
        my_tape.add(s1)
        my_tape.add(s2)
        my_tape.add(s3)
        self.assertEqual(s1, my_tape.read(), ans.format(my_tape.read(), s1))
        s1 = new_string(10)
        my_tape.write(s1)
        self.assertEqual(s1, my_tape.read(), ans.format(my_tape.read(), s1))
        x = my_tape.next()
        self.assertEqual(s2, my_tape.read(), ans.format(my_tape.read(), s2))
        s2 = new_string(10)
        my_tape.write(s2)
        self.assertEqual(s2, my_tape.read(), ans.format(my_tape.read(), s2))
        x = my_tape.next()
        self.assertEqual(s3, my_tape.read(), ans.format(my_tape.read(), s3))
        s3 = new_string(10)
        my_tape.write(s3)
        self.assertEqual(s3, my_tape.read(), ans.format(my_tape.read(), s3))


def new_string(n):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))
        
if __name__ == '__main__':
    unittest.main()
