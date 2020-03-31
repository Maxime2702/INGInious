#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest

import CorrQ as corr
import q


class TestQ(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'Counters') and hasattr(q.Counters, '__init__') and hasattr(q.Counters, 'next'), "Vous n'avez pas nommé la classe ou les méthodes comme demandé.")

    def test_init(self):
        ans = "Votre méthode __init__ ne crée pas les compteurs qu'elle devrait."
        counters = q.Counters(5)
        self.assertEqual(0, counters.next(0), ans)
        self.assertEqual(0, counters.next(1), ans)
        self.assertEqual(0, counters.next(2), ans)
        self.assertEqual(0, counters.next(3), ans)
        self.assertEqual(0, counters.next(4), ans)

    def test_next(self):
        ans = "Votre méthode next ne renvoit pas la valeur supposée de l'un des compteurs."
        counters = q.Counters(10)
        self.assertEqual(0, counters.next(0), ans)
        self.assertEqual(1, counters.next(0), ans)
        self.assertEqual(0, counters.next(1), ans)
        self.assertEqual(2, counters.next(0), ans)
        self.assertEqual(0, counters.next(5), ans)
        self.assertEqual(1, counters.next(1), ans)

    def test_IndexError(self):
        counters = q.Counters(10)
        with self.assertRaises(IndexError):
            counters.next(11)


if __name__ == '__main__':
    unittest.main()
