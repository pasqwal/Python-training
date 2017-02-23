#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module métier de gestion bancaire perso
----------------------------------------


"""


class BusinessError(Exception):
    """
    Exception destinée à identifier des erreurs métier.
    """
    def __init__(self, value, cause=None):
        super(BusinessError, self)\
            .__init__(value + u', caused by ' + repr(cause))
        self.cause = cause

# Python 2 only
#    def __str__(self):
#        return repr(self._value)


class Account:
    def __init__(self, id, balance=100, limit=5000):
        self._id = id
        self._balance = int(balance)
        self._limit = limit

    def deposit(self, value):
        if value >= 0:
            self._balance += value
        else:
            raise ValueError("Select a positive amount for a deposit ")

# methode withdraw_with_decouvert à mettre dans une classe spécialisé
    def withdraw_with_decouvert(self, value):
        if value >= 0:
            new_balance = self._balance - value
            if new_balance <= 5000:
                raise BusinessError("decouvert max atteint", self)
            else:
                self._balance -= value
        else:
            raise ValueError("select a positive amount for a withdraw")

    def withdraw(self, value):
        if 0 < value <= (self._balance + self._limit):
            self._balance -= value
        elif (self._balance + self._limit) < value:
            raise BusinessError("Insufficient funds", self)
        else:
            raise ValueError("Negative value")

    def balance(self):
        return self._balance

    def __str__(self):
        return "le compte {} a un solde de {} euros".format(self._id, self._balance)

    def __repr__(self):
        return "Account {}".format(self._id)


class Person:
    def __init__(self, id, nom, prenom, accounts=[]):
        self._id = id
        self._nom = nom
        self._prenom = prenom
        self._accounts = accounts

    def addAccount(self, Account):
        if len(self._accounts) <= 5:
            self._accounts[Account._id] = Account
        else:
            pass

    def __str__(self):
        return "{} {} dispose de comptes {}".format(self._nom, self._prenom, self._accounts)

class DiffereAccount(Account):
    """
    gestion des comptes a debit differre, qui disposent d'une liste d'operation à executer en fin de mois
    ----------------------------------------

    """
    def __init__(self, id, balance):
        Account.__init__(self, id, balance)
        self._operations = []

    def withdraw(self, value):
        self._operations.append(value)

    def triggerMonthlyAction(self):
        while self._operations:
            #self._balance -= self._operations.pop()
            Account.withdraw(self._operations.pop())

class EpargneAccount(Account):
    """
        gestion des comptes Epargne, qui sont rémunérés d'un certain Taux en fin de mois
        ----------------------------------------

    """
    def __init__(self, id, balance, taux):
        Account.__init__(self, id, balance)
        self._taux = taux

    def triggerMonthlyAction(self):
        #self._balance += self._balance * self._taux
        self.deposit(self._balance * self._taux)

if __name__ == "__main__":
    import doctest
    doctest.testmod()