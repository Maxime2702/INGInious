#!/usr/bin/python3
# -*- coding: utf-8 -*-


def getMax(filename):
	maxvalue = -1
	try: 
		with open ( filename, "r" ) as file:
			for line in file:
				try:
					value = float(line)
					if value >= maxvalue and value >= 0:
						maxvalue = value
				except ValueError:
					pass
	except OSError:
		print ( "Error reading file" )
	return maxvalue
