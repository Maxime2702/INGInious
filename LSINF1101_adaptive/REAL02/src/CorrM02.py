#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Recherche des racines d'une équation a x + b y = c
# Charles Pecheur, septembre 2018

def M02(a, b, c, max):
    solutions = 0

    for x in range(1, max):
        for y in range(1, max):
            for z in range(1, max):
                if x**a + y**yb == z**c:
                    print("x =", x, " y =", y, " z =", z)
                    solutions += 1

    if solutions == 0:
        print("Aucune solution trouvee")
    else:
        print(solutions, "solutions trouvees")
