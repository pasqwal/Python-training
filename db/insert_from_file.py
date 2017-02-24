#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module chargement d'un fichier dans une base
----------------------------------------


"""


# connection soit à une bdd fichier ou une bdd memoire
con = lite.connect('testdb.db')
# con = lite.connect(":memory:")

cursor = con.cursor()
cursor.execute("CREATE TABLE serie IF NOT EXISTS (name_last, age)")