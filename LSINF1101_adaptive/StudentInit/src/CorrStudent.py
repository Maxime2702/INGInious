#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Student:

    def __init__(self, name, surname, birth_date, email):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.email = email

    def __str__(self):
        ans = "Etudiant {} {} né le {}, peut être joint sur {}"
        return ans.format(self.name, self.surname, self.birth_date, self.email)
