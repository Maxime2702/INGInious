#! /usr/bin/python3
# -*- coding: utf-8 -*-

import math

def verify_order(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

def coordinate(commune, all_communes):
    first = 0
    last = len(all_communes)-1
    res = None
    while first<=last and res is None:
        middle = (first + last)//2
        if all_communes[middle][0] == commune:
            res = all_communes[middle][1]
        else:
            if commune < all_communes[middle][0]:
                last = middle-1
            else:
                first = middle+1
    return res

def distance(commune1, commune2, all_communes):
    coord1, coord2 = coordinate(commune1, all_communes), coordinate(commune2, all_communes)
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def tour_distance(l, all_communes):
    return sum([distance(l[i],l[i+1], all_communes) for i in range(-1,len(l)-1)])

def distances(commune, all_communes):
    res = []
    for c in all_communes:
        other_commune = c[0]
        if other_commune != commune:
            res.append((distance(commune, other_commune, all_communes), other_commune))
    return res

def closest(commune, all_communes):
    return sorted([(distance(commune,c[0],all_communes),c[0]) for c in all_communes])[1][1]

def distance_matrix(communes, all_communes):
    return [[distance(c1, c2, all_communes) for c2 in communes] for c1 in communes]
