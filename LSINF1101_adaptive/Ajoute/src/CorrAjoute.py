#!/usr/bin/python3
# -*- coding: utf-8 -*-


def ajoute ( l, v ):
  for i in l:
    if i == v:
      return
  l.append ( v )