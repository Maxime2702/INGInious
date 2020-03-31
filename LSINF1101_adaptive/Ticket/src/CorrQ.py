#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Ticket :

    __prochain_numero = 1  # variable de classe pour générer le numéro du ticket

    def __init__(self) :
        """
        @pre  -
        @post Crée un ticket avec un nouveau numéro.
              Les numéros sont attribués séquentiellement à partir de 1. 
        """
        self.__numero = Ticket.__prochain_numero
        Ticket.__prochain_numero += 1


    def numero(self):
        """
        @pre  -
        @post retourne le numero de billet
        """
        return self.__numero

