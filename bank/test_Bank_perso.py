#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module pour tester les cas d'usage du module bank.Bank_perso
----------------------------------------


"""

#TODO: installer le module Coverage

import unittest
from bank import Bank_perso as bank


class TestCreateAccount(unittest.TestCase):

    def testBasicAccount(self):
        account = bank.Account('012345')
        self.assertEqual(100, account.balance())

    def testAccountWithBalance(self):
        account = bank.Account('012345', 500)
        self.assertEqual(500, account.balance())


class TestDeposit(unittest.TestCase):

    def setUp(self):
        self.account = bank.Account('012345', 500)

    def testBasicDeposit(self):
        self.account.deposit(100)
        self.assertEqual(600, self.account.balance())

    def tearDown(self):
        del self.account

if __name__ == "__main__":
    unittest.main()
