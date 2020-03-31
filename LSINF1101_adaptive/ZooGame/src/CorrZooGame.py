#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, name):
        self.name = name
        self.diurnal = None
        self.nb_legs = None
        self.asleep = False

    def sleep(self):
        if self.asleep:
            raise RuntimeError("Tried to sleep while already sleeping")
        self.asleep = True

    def wake_up(self):
        if not self.asleep:
            raise RuntimeError("Tried to wake up while already awake")
        self.asleep = False


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4

    def roar(self):
        print("ROARRR!!!")


class Owl(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.diurnal = False
        self.nb_legs = 2

    def fly(self):
        pass


class Giraffe(Animal):
    def __init__(self, name, neck_length):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4
        if (isinstance(neck_length, int) or isinstance(neck_length, float)) and neck_length >= 0:
            self.neck_length = neck_length
        else:
            raise ValueError("{} is not a valid neck length".format(neck_length))

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Tried to add something else than an animal in the zoo")
        self.animals.append(animal)


def create_my_zoo():
    my_zoo = Zoo()
    my_zoo.add_animal(Lion("Jesus"))
    my_zoo.add_animal(Owl("Irma"))
    my_zoo.add_animal(Giraffe("Nick", 1.0))
    my_zoo.add_animal(Giraffe("Olga", 1.5))
    return my_zoo
