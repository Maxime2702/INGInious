#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fine(speed_authorized, actual_speed):
    if actual_speed > speed_authorized:
        speed = actual_speed - speed_authorized
        if speed < 3: penalty = 12.5
        else:
            penalty = speed * 5
            if speed > 10: penalty *= 2
        return penalty
    else: return 0
