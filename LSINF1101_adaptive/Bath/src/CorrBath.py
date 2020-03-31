#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import ceil

filled_time = 80/11

water_vol = 0
for i in range(ceil(filled_time)):
    water_vol += 12
    water_vol -= 1
