#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3 as lite

# SQL_CREATE = "CREATE TABLE IF NOT EXISTS sncf (date, nom_train, ponctualite)"
SQL_CREATE = "CREATE TABLE IF NOT EXISTS {table} ({fields}) "
# SQL_INSERT = "INSERT INTO sncf values(?, ?, ?)"
SQL_INSERT = "INSERT INTO {table} values({values})"

class CreateDb:
    def __init__(self, name=':memory:', path=''):
        self._name = name
        self._path = path
        self._connection = lite.connect(path + self._name)
        self.cursor = self._connection.cursor()

    def createTable(self, tablename='test', liste_champs=('champ_test')):
        self.cursor.execute(SQL_CREATE.format(table=tablename, fields=liste_champs))

    def insertIntoTable(self, tablename='test', values=('record1',)):
        format_nb_champs = ','.join('?'*len(values))
        print(SQL_INSERT.format(table=tablename, values=format_nb_champs))
        self.cursor.executemany(SQL_INSERT.format(table=tablename, values=format_nb_champs), values)

    def getDataFromTable(self, tablename='test'):
        self.cursor.execute("SELECT * FROM {}".format(tablename))
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self._connection.close()

if __name__ == "__main__":
    try:
        db = CreateDb()
        db.createTable()
        db.insertIntoTable()
        rows = db.getDataFromTable()
        for row in rows:
            print(row)
    finally:
        db.close()