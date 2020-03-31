#!/usr/bin/python3
# -*- coding: utf-8 -*-


def recherche ( m, v ):
  for l in m:
    for e in l:
      if e == v:
        return True
  return False