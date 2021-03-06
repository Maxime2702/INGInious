#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Item :

    def __init__(self,author,title,serial):
        """
        Méthode d'initialisation.
        @pre  author et title sont des valeurs de type String
              serial est un entier > 0
        @post Une instance de la classe est créée, et représente un objet ayant
              comme auteur author, comme titre title et comme numéro de série serial
        """
        self.__author = author
        self.__title = title
        self.__serial = serial
        
    def __str__(self):
        """
        Méthode de conversion en string.
        @pre  -
        @post le string retourné contient une représentation de cet objet sous la
              forme: [numéro de série] Auteur, Titre
        """
        return "[{}] {}, {}".format(self.__serial,self.__author,self.__title)
              
class CD(Item):

    __nextid = 100000
    
    def __init__(self,author,title,duration):
        """
        Méthode d'initialisation.
        @pre  author et title sont des valeurs de type String
              duree est un entier > 0 représentant un temps en secondes
        @post Une instance de la classe est créée, et représente un objet ayant
              comme auteur author, comme titre title, comme duree duration,
              et un numéro de série unique, supérieur à 10.000
        """
        super().__init__(author,title,self.__nextid)
        self.__duration = duration
        CD.__nextid += 1

    def __str__(self):
        """
        Méthode de conversion en string.
        @pre  -
        @post le string retourné contient une représentation de cet objet sous la
              forme: "[numéro de série] Auteur, Titre (Duration s)"
        """
        return super().__str__() + " (" + str(self.__duration) + " s)"
