#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrDestroy as corr
import destroy


class TestDestroy(unittest.TestCase):
    def test_method_exist(self):
        try:
            destroy.Cratos(None)
        except NameError:
            self.assertTrue(False, _("Does the class `Cratos` exist?"))
        try:
            destroy.Drauf(100)
        except NameError:
            self.assertTrue(False, _("Does the class `Drauf` exist?"))
        try:
            destroy.Weapon(100)
        except NameError:
            self.assertTrue(False, _("Does the class `Weapon` exist?"))

        cratos = destroy.Cratos(None)
        self.assertTrue(hasattr(cratos, "__init__"), _("Your class `Cratos` does not have a method `__init__`."))
        self.assertTrue(hasattr(cratos, "weapon"), _("Your class `Cratos` does not have an attribute `weapon`."))
        self.assertTrue(hasattr(cratos, "set_weapon"), _("Your class `Cratos` does not have a method `set_weapon`."))
        self.assertTrue(hasattr(cratos, "hit"), _("Your class `Cratos` does not have a method `hit`."))

        weapon = destroy.Weapon(10)
        self.assertTrue(hasattr(weapon, "__init__"), _("Your class `Weapon` does not have a method `__init__`."))
        self.assertTrue(hasattr(weapon, "attack"), _("Your class `Weapon` does not have an attribute `attack`."))

        drauf = destroy.Drauf(10)
        self.assertTrue(hasattr(drauf, "__init__"), _("Your class `Drauf` does not have a method `__init__`."))
        self.assertTrue(hasattr(drauf, "life"),  _("Your class `Drauf` does not have an attribute `life`."))
        self.assertTrue(hasattr(drauf, "get_hit"),  _("Your class `Drauf` does not have a method `get_hit`."))

    def test_constructor(self):
        atk = random.randint(0, 150)
        weapon = destroy.Weapon(atk)
        weaponCorr = corr.Weapon(atk)
        self.assertEqual(weapon.attack, weaponCorr.attack, _("The Weapon constructed has not the good attack, it has {}"
                                                             " instead of {}").format(weapon.attack, weaponCorr.attack))

        cratos = destroy.Cratos(weapon)
        cratosCorr = corr.Cratos(weapon)
        self.assertEqual(cratos.weapon, cratosCorr.weapon, _("The Cratos constructed has not the good weapon, make sure"
                                                             " you set it in the constructor"))

        life = random.randint(0, 150)
        drauf = destroy.Drauf(life)
        draufCorr = corr.Drauf(life)
        self.assertEqual(draufCorr.life, drauf.life, _("The Drauf constructed has not the good life, it has {} instead"
                                                       " of {}").format(drauf.life, draufCorr.life))

    def test_combat(self):
        atk = random.randint(5, 10)
        life = random.randint(100, 150)
        weapon = destroy.Weapon(atk)
        weaponCorr = corr.Weapon(atk)
        cratos = destroy.Cratos(weapon)
        cratosCorr = corr.Cratos(weapon)
        drauf = destroy.Drauf(life)
        draufCorr = corr.Drauf(life)

        for i in range(0, 5):
            if i == 1:
                cratos.hit(drauf)
                cratosCorr.hit(draufCorr)
            if i == 2:
                atk = random.randint(11, 20)
                weapon2 = destroy.Weapon(atk)
                cratos.set_weapon(weapon2)
                cratosCorr.set_weapon(weapon2)
            if i == 3:
                cratos.hit(drauf)
                cratosCorr.hit(draufCorr)

            self.assertEqual(weapon.attack, weaponCorr.attack, _("The Weapon has not the good attack, it has {} instead"
                                                                 " of {}").format(weapon.attack, weaponCorr.attack))
            self.assertEqual(cratos.weapon, cratosCorr.weapon, _("The Cratos has not the good weapon, make sure set_"
                                                                 "weapon is correct"))
            self.assertEqual(draufCorr.life, drauf.life, _("The Drauf has not the good life, it has {} instead of "
                                                           "{}").format(drauf.life, draufCorr.life))

if __name__ == '__main__':
    unittest.main()
