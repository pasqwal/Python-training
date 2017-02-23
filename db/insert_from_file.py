#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module chargement d'un fichier dans une base
----------------------------------------


"""

import sqlite3 as lite

class CreateDb:
    def __init__(self, name='testdb.db'):
        self._name = name
        self._connection = lite.connect(self._name)
        self.cursor = self._connection.cursor()

    def execute(self):
        pass

# connection soit à une bdd fichier ou une bdd memoire
con = lite.connect('testdb.db')
#con = lite.connect(":memory:")

cursor = con.cursor()
cursor.execute("CREATE TABLE serie IF NOT EXISTS (name_last, age)")