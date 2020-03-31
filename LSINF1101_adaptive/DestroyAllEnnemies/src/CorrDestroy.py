#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Character:
    def __init__(self):
        self.life = 100
        self.attack_point = 10

    def attack(self, target):
        target.get_hit(self.attack_point)

    def get_hit(self, damage):
        self.life -= damage


class Cratos(Character):
    def __init__(self):
        Character.__init__(self)
        self.experience = 0

    def gain_XP(self, amount):
        self.experience += amount
        while self.experience >= 10:
            self.experience -= 10
            self.attack_point += 1


class Drauf(Character):
    def __init__(self, life, attack_point):
        Character.__init__(self)
        self.life = life
        self.attack_point = attack_point
