#!/usr/bin/python3
# -*- coding: utf-8 -*-


############################
# CircularLinkedList class #
############################

class CircularLinkedList :
    
    ### BEGIN inner class Node ###

    class Node:

        def __init__(self, cargo=None, next=None):
            """
            Initialises a new Node object.
            @pre:  -
            @post: A new Node object has been initialised.
                   A node can contain a cargo and a reference to another node.
                   If none of these are given, the node is initialised with empty cargo (None) and no reference (None).
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

        def next(self):
            """
            Returns the next node to which this node links.
            @pre:  -
            @post: Returns the node to which this node is linked with its next pointer, or None if that pointer is None.
            """
            return self.__next

        def set_next(self,node):
            """
            Sets the next node to which this node links to a new node.
            @pre:  -
            @post: The node to which this node is linked next, has been set to the new node passed as parameter.
                   Can also be set to None by passing None as parameter.
            """
            self.__next = node

        def __str__(self):
            """
            Returns a string representation of the cargo of this node.
            @pre:  self is a (possibly empty) Node object.
            @post: Returns a print representation of the cargo contained in this Node.
            """
            return str(self.value())
    
    ### END inner class Node ###
    
    def __init__(self):
        """
        Initialises a new empty circular linked list.
        @pre:  -
        @post: A new circular linked list with no nodes has been initialised.
               The first pointer refers to None.
        """
        self.__first = None       # pointer to the first node in the circular linked list
        self.__last = None        # pointer to the last node in the circular linked list

    def first(self):
        """Accessor method which returns the first node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the first node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__first

    def last(self):
        """Accessor method which returns the last node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the last node of this circular linked list,
               or None if the circular linked list contains no nodes.
        """
        return self.__last

    def add(self, cargo):
        """ 
        Adds a new Node with given cargo to the front of this circular linked list. 
        @pre: self is a (possibly empty) CircularLinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the circular linked list.
               The head of the list now points to this new node.
               The last node now points to this new node.
        """
        node = self.Node(cargo,self.first())
        self.__first = node
        if self.last() == None :   # when this was the first element being added,
            self.__last = node     # set the last pointer to this new node
        self.last().set_next(node)

    def remove(self,cargo):
        """
        Removes a node with given cargo from the circular linked list.
        Leaves the list intact if already empty. 
        @pre:  -
        @post: A node with given cargo was removed from the circular linked list.
               The removed node, with next pointer set to None, is returned as result.
               In case multiple nodes with this cargo exist, only one is removed. 
               The list is left intact if no such node exists or if the list is empty.
               In that case, None is returned as result.
        """
        previous = self.last()
        node = self.first()
        # in case of empty list, return nothing
        if node is None :
            return None
        # if the list has only 1 element and this is the element to be removed
        elif previous is self.first() and node.value() == cargo :
            self.__first = None  # set head of the circular linked list to None 
            self.__last = None   # set last of the circular linked list to None
            node.set_next(None)  # remove next pointer from the found node
            return node          # return the removed node
        # loop to remove first occurence when list has more than one element 
        else :            
            while True:
                # Remove and return node if found 
                if node.value() == cargo :             # node to be removed found
                    previous.set_next(node.next())     # jump over found node
                    if node is self.first() :          # if found node is __first
                        self.__first = previous.next() # set __first to next one
                    if node is self.last() :           # if found node is __last
                        self.__last = previous         # set __last to previous
                    node.set_next(None) # remove next pointer from the found node
                    return node         # return the removed node
                # If not yet found, continue from next node
                previous = node
                node = node.next()
                # exit loop if we are back at the first node
                if node is self.first(): 
                    break

    def removeAll(self,cargo):
        """
        Removes all nodes with given cargo from the circular linked list.
        Leaves the list intact if already empty. 
        """
        while True: # remove until cargo no longer found in list
            if self.remove(cargo) == None :
                break
