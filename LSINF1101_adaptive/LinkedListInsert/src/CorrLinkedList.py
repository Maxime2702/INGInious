#!/usr/bin/python3
# -*- coding: utf-8 -*-


class LinkedList :    

    class Node:
        def __init__(self, cargo=None, next=None):
            """
            Initialises a new Node object.
            @pre:  -
            @post: A new Node object has been initialised.
                   A node can contain a cargo and a reference to another node.
                   If none of these are given, a node with empty cargo (None) and no reference (None) is created.
            """
            self.__cargo = cargo
            self.__next  = next

        def value(self):
            """
            Returns the value of the cargo contained in this node.
            @pre:  -
            @post: Returns the value of the cargo contained in this node, or None if no cargo  was put there.

            """
            return self.__cargo

        def __str__(self):
            """
            Returns a string representation of the cargo of this node.
            @pre:  self is possibly empty Node object
            @post: returns a print representation of the cargo contained in this Node
            """
            return str(self.value())

        def next(self):
            return self.__next

        def set_next(self, node):
            self.__next = node

    def __init__(self, lst=[]):
        self.__length = 0
        self.__head = None
        self.__last = None
        for e in lst :
            self.add_to_end(e)

    def size(self):
        """
        Returns the number of nodes contained in this linked list
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list
        """
        return self.__length

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the front of this linked list.
        @pre: self is a (possibly empty) LinkedList
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented.
               The head of the list now points to this new node.
        """
        node = self.Node(cargo,self.__head)
        if self.__head is None :     # when this is the first element being added,
            self.__last = node  
        self.__head = node
        self.__length += 1
        
    def __repr__(self):
        res = ""
        h = self.__head
        while h is not None:
            res += str(h.value()) + " "
            h = h.next()
        return res
        
    def __str__(self):
        res = ""
        h = self.__head
        while h is not None:
            res += str(h.value()) + " "
            h = h.next()
        return res
        
    def first(self):
        return self.__head

    def remove(self):
        """
        Removes the node at the start of the list. Leaves the list intact if already empty.
        """
        if self.__head is not None:
            self.__length -= 1
            self.__head = self.__head.next()
            if self.__length == 0:       # when there are no more elements in the list,
                self.__last = None       # remove the pointer to the last element


    def add_to_end(self, cargo):
        if self.__length == 0 :        # si la liste est encore vide,
            self.add(cargo)            # ajouter à la fin correspond au ajouter au début
        else :                         # si la liste contient déjà au moins un noeud (et donc une dernier noeud)
            node = self.Node(cargo)
            self.__last.set_next(node) # make the current last node point to this new node
            self.__last = node         # set the last node reference to this new node
            self.__length += 1   
    

    def __eq__(self, lst):
        h1 = self.__head
        h2 = lst.first()
        for i in range(self.__length+1):
            if h1 is None:
                if h2 is None:
                    return True
                else:
                    break
            if h1.value() != h2.value():
                break
            h1 = h1.next()
            h2 = h2.next()
        return False
        
    def insert(self,s):
        if self.size() == 0 :
            self.add(s)
            return
        elif s < self.first().value() :
            self.add(s)
            return
        else :
            # ne pas oublier d'incrémenter la taille de la liste
            self.__length += 1
            # ensuite chercher le bon endroit à insérer le nouveau noeud
            current = self.first()
            while (current.next() is not None):
                if s < current.next().value():
                    # insérer entre current et current.next
                    n = self.Node(s, current.next())
                    current.set_next(n)
                    return;
                current = current.next()
            # si on arrive ici on est au dernier élément
        current.set_next=self.Node(s, None)  
