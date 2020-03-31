#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Employee:
    def __init__(self, pay):
        self.pay = pay
        self.money = 0

    def receive_salary(self, much):
        self.money += much

class EmployeeDidntWorked(Exception):
    pass

class EmployeeWorkedNegatively(Exception):
    pass

class EmployeeWorkedTooMuch(Exception):
    pass

class PayIsNegative(Exception):
    pass

class PayIsTooBig(Exception):
    pass

def pay_employee(employee, hours):
    if hours == 0: raise EmployeeDidntWorked()
    if hours < 0: raise EmployeeWorkedNegatively()
    if hours > 744: raise EmployeeWorkedTooMuch()
    if employee.pay < 0: raise PayIsNegative()
    if employee.pay > 100: raise PayIsTooBig()
    employee.receive_salary(hours * employee.pay)
