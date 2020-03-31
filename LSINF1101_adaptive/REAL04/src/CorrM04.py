#! /usr/bin/python3
# -*- coding: utf-8 -*-

def is_adn(text):
	for c in text:
		if c.lower() not in ['a', 't', 'c', 'g']: return False
	return True

def positions(text,car):
	res = []
	i = 0
	up_b = len(text) - len(car) + 1
	while i < up_b:
		if text[i: i+len(car)].upper() == car.upper():
			res.append(i)
		i += 1
	return res

def distance_h(text1,text2):
	diffs = 0
	for ch1, ch2 in zip(text1, text2):
		if ch1 != ch2:
			diffs += 1
	return diffs

def plus_long_palindrome(text):
    text = text.lower()
    res = ''
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                if len(chunk) > len(res):
                    res = chunk
    return res
