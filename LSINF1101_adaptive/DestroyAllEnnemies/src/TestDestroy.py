#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrDestroy as corr
import destroy


class TestDestroy(unittest.TestCase):
    def test_method_exist(self):
        try:
            destroy.Character()
        except NameError:
            self.assertTrue(False, _("Does the class `Character` exist?"))
        try:
            destroy.Cratos()
        except NameError:
            self.assertTrue(False, _("Does the class `Cratos` exist?"))
        try:
            destroy.Drauf(100, 100)
        except NameError:
            self.assertTrue(False, _("Does the class `Drauf` exist?"))

        character = destroy.Character()
        self.assertTrue(hasattr(character, "life"), _("Your class `Character` does not have an attribute `life`."))
        self.assertTrue(hasattr(character, "attack"), _("Your class `Character` does not have a method `attack`."))
        self.assertTrue(hasattr(character, "get_hit"), _("Your class `Character` does not have a method `get_hit`."))
        self.assertTrue(hasattr(character, "attack_point"), _("Your class `Character` does not have an attribute"
                                                              " `attack_point`."))

        cratos = destroy.Cratos()
        self.assertTrue(hasattr(cratos, "gain_XP"), _("Your class `Cratos` does not have a method `gain_XP`."))

        drauf = destroy.Drauf(10,10)
        self.assertFalse(hasattr(drauf, "gain_XP"), _("Your class `Drauf` have a method `gain_XP` which it shouldn't"
                                                      " have."))
        self.assertFalse(hasattr(drauf, "experience"), _("Your class `Drauf` have an attribute `experience` which it"
                                                         " shouldn't have."))

    def test_constructor(self):
        cratos = destroy.Cratos()
        cratosCorr = corr.Cratos()
        self.assertEqual(cratosCorr.life, cratos.life, _("The Cratos constructed has not the good life, it has {}"
                                                         " instead of {}")
                         .format(cratos.life, cratosCorr.life))
        self.assertEqual(cratosCorr.attack_point, cratos.attack_point, _("The Cratos constructed has not the good "
                                                                         "attack_point, it has {} instead of {}")
                         .format(cratos.attack_point, cratosCorr.attack_point))
        self.assertEqual(cratosCorr.experience, cratos.experience, _("The Cratos constructed has not the good"
                                                                     " experience, it has {} instead of {}")
                         .format(cratos.experience, cratosCorr.experience))

        life = random.randint(0, 150)
        atk = random.randint(0, 150)
        drauf = destroy.Drauf(life, atk)
        draufCorr = corr.Drauf(life, atk)
        self.assertEqual(draufCorr.life, drauf.life, _("The Drauf constructed has not the good life, it has {} instead"
                                                       " of {}")
                         .format(drauf.life,draufCorr.life))
        self.assertEqual(draufCorr.attack_point, drauf.attack_point, _("The Drauf constructed has not the good attack"
                                                                       "_point, it has {} instead of {}")
                         .format(drauf.attack_point,draufCorr.attack_point))

    def test_gain_XP(self):
        cratos = destroy.Cratos()
        cratosCorr = corr.Cratos()
        strAtk = _("The Cratos has not the good attack_point, it has {} instead of {}")
        strXP = _("The Cratos has not the good experience, it has {} instead of {}")
        gain = [5, 12, 3, 33]
        self.assertEqual(cratosCorr.attack_point, cratos.attack_point, strAtk.format(cratos.attack_point,
                                                                                     cratosCorr.attack_point))
        self.assertEqual(cratosCorr.experience, cratos.experience, strXP.format(cratos.experience,
                                                                                cratosCorr.experience))

        for i in gain:
            cratos.gain_XP(i)
            cratosCorr.gain_XP(i)
            self.assertEqual(cratosCorr.attack_point, cratos.attack_point, strAtk.format(cratos.attack_point,
                                                                                         cratosCorr.attack_point))
            self.assertEqual(cratosCorr.experience, cratos.experience, strXP.format(cratos.experience,
                                                                                    cratosCorr.experience))

    def test_combat(self):
        cratos = destroy.Cratos()
        cratosCorr = corr.Cratos()
        drauf = destroy.Drauf(100, 1)
        draufCorr = corr.Drauf(100, 1)
        strAtk = _("The Cratos has not the good attack_point, it has {} instead of {}")
        strLife = _("The Cratos has not the good life, it has {} instead of {}")
        strXP = _("The Cratos has not the good experience, it has {} instead of {}")
        strAtkDrauf = _("The Drauf has not the good attack_point, it has {} instead of {}")
        strLifeDrauf = _("The Drauf has not the good life, it has {} instead of {}")

        for i in range(0, 10):
            if i == 0:
                cratos.attack(drauf)
                cratosCorr.attack(draufCorr)
            if i == 1:
                cratos.attack(drauf)
                cratosCorr.attack(draufCorr)
            if i == 2:
                drauf.attack(cratos)
                draufCorr.attack(cratosCorr)
            if i == 3:
                cratos.gain_XP(7)
                cratosCorr.gain_XP(7)
            if i == 4:
                cratos.attack(drauf)
                cratosCorr.attack(draufCorr)
            if i == 5:
                cratos.gain_XP(23)
                cratosCorr.gain_XP(23)
            if i == 6:
                cratos.attack(drauf)
                cratosCorr.attack(draufCorr)
            if i == 7:
                drauf.attack(cratos)
                draufCorr.attack(cratosCorr)
            self.assertEqual(cratosCorr.attack_point, cratos.attack_point, strAtk.format(cratos.attack_point,
                                                                                         cratosCorr.attack_point))
            self.assertEqual(cratosCorr.experience, cratos.experience, strXP.format(cratos.experience,
                                                                                    cratosCorr.experience))
            self.assertEqual(cratosCorr.life, cratos.life, strLife.format(cratos.life, cratosCorr.life))
            self.assertEqual(drauf.life, draufCorr.life, strLife.format(drauf.life, draufCorr.life))
            self.assertEqual(drauf.attack_point, draufCorr.attack_point, strAtk.format(drauf.attack_point,
                                                                                       draufCorr.attack_point))


if __name__ == '__main__':
    unittest.main()
