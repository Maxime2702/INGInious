#!/usr/bin/python3
# -*- coding: utf-8 -*-


def match(s1, s2):
	"""
	pre: s2 pas plus long que s1, s2 ne contient pas ?
	post: retourne true si s1 matche le début de la chaine s2 et false sinon
	"""
	for i in range(len(s1)):
		if s1[i] != "?":
			if s1[i] != s2[i]:
				return False
	return True


def positions(p, s):
	return [i for i in range(len(s)-len(p)+1) if match(p.lower(),s[i:].lower()) ]

