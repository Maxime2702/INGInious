#!/usr/bin/python3
# -*- coding: utf-8 -*-

def give_money(borrowed_money, from_person, to_person, amount):
    if type(borrowed_money) != dict:
        raise ValueError("Invalid type for `borrowed_money`: `dict` expected")
    if type(from_person) != str or type(to_person) != str:
        raise ValueError("Invalid type for people's names: strings expected")
    if type(amount) != int and type(amount) != float:
        raise ValueError("Invalid type for the amount of money: `int` or `float` expected")
    if from_person == to_person:
        raise ValueError("Tried to give money to oneself")

    if to_person in borrowed_money:
        if from_person in borrowed_money[to_person]:
            borrowed_money[to_person][from_person] += amount
        else:
            borrowed_money[to_person][from_person] = amount
    else:
        borrowed_money[to_person] = {from_person: amount}

    if from_person in borrowed_money:
        if to_person in borrowed_money[from_person]:
            borrowed_money[from_person][to_person] -= amount
        else:
            borrowed_money[from_person][to_person] = -amount
    else:
        borrowed_money[from_person] = {to_person: -amount}

def total_money_borrowed(borrowed_money):
    if type(borrowed_money) != dict:
        raise ValueError("Invalid type for `borrowed_money`: `dict` expected")

    sum = 0.0
    for name1 in borrowed_money:
        for name2 in borrowed_money[name1]:
            if borrowed_money[name1][name2] > 0:
                sum += borrowed_money[name1][name2]
    return sum

borrowed_money = {}
mark = "Mark"; bill = "Bill"; steve = "Steve"; serguei = "Serguei"; larry = "Larry"; linus = "Linus"
million = 1000000
give_money(borrowed_money, mark, bill, 2*million)
give_money(borrowed_money, mark, steve, 2*million)
give_money(borrowed_money, serguei, bill, 5*million)
give_money(borrowed_money, bill, larry, 6*million)
give_money(borrowed_money, larry, linus, 5.5)
give_money(borrowed_money, steve, mark, 2*million)
