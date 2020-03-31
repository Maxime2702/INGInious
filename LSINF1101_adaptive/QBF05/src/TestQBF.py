#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQBF as corr
import qbf


class TestQBF(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(qbf, 'matrix_for_traces'), _("Vous n'avez pas fourni la méthode matrix_for_traces."))

    def test_hard_l(self):
        t1 = [(1.0,(10.10,20.0)),(3.0,(10.50,20.30)),(5.0,(11.0,21))]
        t2 = [(1.0,(15.00,15.0)),(2.0,(12.00,17.00)),(3.0,(10.50,20)),(4.0,(12.0,21.0))]
        ans = _("Avec les traces: {} \n et les thétas {}:\n\nVous avez renvoyé {} plutot que {}.")
        stu_ans = qbf.matrix_for_traces([t1, t2], 0, 0)
        corr_ans = [[0, 0], [0,0]]
        self.assertEqual(corr_ans, stu_ans, ans.format([t1,t2], (0.0, 0.0), stu_ans, corr_ans))

    def test_(self):
        t1 = [(1.0,(10.10,20.0)),(3.0,(10.50,20.30)),(5.0,(11.0,21))]
        t2 = [(1.0,(15.00,15.0)),(2.0,(12.00,17.00)),(3.0,(10.50,20)),(4.0,(12.0,21.0))]
        ans = _("Avec les traces: {} \n et les thétas {}:\n\nVous avez renvoyé {} plutot que {}.")
        stu_ans = qbf.matrix_for_traces([t1, t2], 0, 1)
        corr_ans = [[1, 1], [1,1]]
        self.assertEqual(corr_ans, stu_ans, ans.format([t1,t2], (0, 1), stu_ans, corr_ans))

    def test_(self):
        t1 = [(1.0,(10.10,20.0)),(3.0,(10.50,20.30)),(5.0,(11.0,21))]
        t2 = [(1.0,(15.00,15.0)),(2.0,(12.00,17.00)),(3.0,(10.50,20)),(4.0,(12.0,21.0))]
        t3 = [(1.0,(15.00,15.0)),(3.0,(16.0,21.0)),(5.0,(20.0,21.0))]
        ans = _("Avec les traces: {} \n et les thétas {}:\n\nVous avez renvoyé {} plutot que {}.")
        stu_ans = qbf.matrix_for_traces([t1, t2, t3], 0, 1)
        corr_ans = [[1,1,0],[1,1,1],[0,1,1]]
        self.assertEqual(corr_ans, stu_ans, ans.format([t1,t2], (0, 1), stu_ans, corr_ans))


if __name__ == '__main__':
    unittest.main()
