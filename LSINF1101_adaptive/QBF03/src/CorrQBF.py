#!/usr/bin/python3
# -*- coding: utf-8 -*-


def chiffres_pairs(n):
    """
    pre: n entier >= 0
    post: retourne True si le nombre de chiffres de n est pair, False sinon
    """
    return est_pair(nombre_chiffres(n))

def nombre_chiffres(n):
    """
    pre: n entier >= 0
    post: retourne le nombre de chiffres de n
    """
    c = 1
    while n >= 10:
        c += 1
        n //= 10
    return c

def est_pair(n):
    """
    pre: n entier
    post: retourne True si n est pair, False sinon
    """
    return n%2 == 0
