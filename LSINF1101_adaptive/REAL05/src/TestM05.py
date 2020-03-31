#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrM05 as corr
import sorted_belgian_communes

communes = [('v0', (0, 0)), ('v1', (52.42, 67.74)), ('v2', (random.uniform(50.5, 70.9), random.uniform(1.5, 1.9))), ('v3', (random.uniform(50.5, 70.9), random.uniform(1.5, 1.9))), ('v4', (random.uniform(50.5, 70.9), random.uniform(1.5, 1.9)))]

class TestM05(unittest.TestCase):
    def test_exist(self):
#        self.assertTrue(hasattr(sorted_belgian_communes, 'verify_order') and hasattr(sorted_belgian_communes, 'coordinate') and hasattr(sorted_belgian_communes, 'distance') and hasattr(sorted_belgian_communes, 'distances') and hasattr(sorted_belgian_communes, 'closest') and hasattr(sorted_belgian_communes, 'distance_matrix'), ("Vous n'avez pas fourni les fonctions demandées."))
        self.assertTrue(hasattr(sorted_belgian_communes, 'verify_order') and hasattr(sorted_belgian_communes, 'coordinate') and hasattr(sorted_belgian_communes, 'distance') and hasattr(sorted_belgian_communes, 'tour_distance') and hasattr(sorted_belgian_communes, 'closest'), ("Vous n'avez pas fourni les fonctions demandées."))

    def test_verify_order(self):
        ans = _("Vote fonction vérifiant l'ordre ne renvoit pas les valeurs souhaitées. {} à la place de {}.")
        order_ok = [('test0', (2, 2)), ('test1', (0, 0)), ('test2', (1, 1))]
        stu_ans = sorted_belgian_communes.verify_order(order_ok)
        self.assertEqual(True, stu_ans, ans.format(stu_ans, True))
        order_nok = [('test3', (2, 2)), ('test1', (0, 0)), ('test2', (1, 1))]
        stu_ans = sorted_belgian_communes.verify_order(order_nok)
        self.assertEqual(False, stu_ans, ans.format(stu_ans, False))

    def test_coordinate(self):
        ans = _("Vote fonction renvoyant les coordonnées ne renvoit pas les valeurs souhaitées. {} à la place de {}.")
        for e in communes:
            stu_ans = sorted_belgian_communes.coordinate(e[0], communes)
            corr_ans = e[1]
            self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))

    def test_distance(self):
        ans = _("Vote fonction renvoyant la distance entre 2 communes ne renvoit pas les valeurs souhaitées pour les communes {} avec comme valeur renvoyée: {} alors qu'on attendait {}")
        for e in communes:
            for c in communes:
                stu_ans = sorted_belgian_communes.distance(e[0], c[0], communes)
                corr_ans = corr.distance(e[0], c[0], communes)
                self.assertEqual(corr_ans, stu_ans, ans.format([e[0], c[0]] ,stu_ans, corr_ans))

    def test_tour_distance(self):
        ans = _("Vote fonction tour_distance ne renvoit pas les valeurs souhaitées pour les communes {} avec comme valeur renvoyée: {} alors qu'on attendait {}")
        communes = [sorted_belgian_communes.all_communes[i][0] for i in [random.randint(0,len(sorted_belgian_communes.all_communes)-1) for _ in range(4)]]
        stu_ans = sorted_belgian_communes.tour_distance(communes, sorted_belgian_communes.all_communes)
        corr_ans = corr.tour_distance(communes, sorted_belgian_communes.all_communes)
        self.assertEqual(corr_ans, stu_ans, ans.format(communes ,stu_ans, corr_ans))

#    def test_distances(self):
#        ans = _("Vote fonction renvoyant les distances par rapport à une commune ne renvoit pas les valeurs souhaitées. {} à la place de {}.")
#        for e in communes:
#            stu_ans = sorted_belgian_communes.distances(e[0], communes)
#            corr_ans = corr.distances(e[0], communes)
#            self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))

    def test_closest(self):
        ans = _("Vote fonction renvoyant les communes les plus proches d'une autre commune ne renvoient pas les valeurs souhaitées. {} à la place de {}.")
        for c in communes:
            stu_ans = sorted_belgian_communes.closest(c[0], communes)
            corr_ans = corr.closest(c[0], communes)
            self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))

#    def test_distance_matrix(self):
#        ans = _("Vote fonction renvoyant les distances sous forme de matrice ne renvoit pas les valeurs souhaitées. {} à la place de {}.")
#        l = ['v0', 'v1', 'v2']
#        stu_ans = sorted_belgian_communes.distance_matrix(l, communes)
#        corr_ans = corr.distance_matrix(l, communes)
#        self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__

