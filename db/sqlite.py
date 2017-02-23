#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module sqlite
----------------------------------------
peut se charger en memoire
Utile pour tester les models de connections aux bases

"""

import sqlite3 as lite

# connection soit à une bdd fichier ou une bdd memoire
#con = lite.connect('testdb.db')
con = lite.connect(":memory:")

cursor = con.cursor()
cursor.execute("CREATE TABLE people IF NOT EXISTS (name_last, age)")

# INSERTION
who = "Yoda"
age = 800
cursor.execute("INSERT INTO people VALUES (?,?)", (who, age))

# EXTRACT
cursor.execute("SELECT * from people where name_last=? and age = ?", (who, age))
row	= cursor.fetchall()
for record in row:
    print("people is {} aged {}".format(record[0], record[1]))



