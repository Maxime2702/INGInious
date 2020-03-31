#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Employe:

    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def __str__(self):
        return "{} : {}".format(self.nom, self.salaire)

    def augmente(self, pourcentage):
        self.salaire += self.salaire * pourcentage / 100
        return self