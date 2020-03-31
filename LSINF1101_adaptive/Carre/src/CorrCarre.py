#!/usr/bin/python3
# -*- coding: utf-8 -*-


def carre(n):
  l = []
  t = 0
  for i in range(n):
    l2 = []
    for j in range(n):
      l2.append ( t )
      t += 1
    l.append ( l2 )
  return l