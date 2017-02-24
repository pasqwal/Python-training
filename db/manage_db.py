#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This Module allows easy db management of sqlite
----------------------------------------


"""

import sqlite3 as lite

SQL_CREATE = "CREATE TABLE IF NOT EXISTS {table} ({fields}) "
SQL_INSERT = "INSERT INTO {table} values({values})"

class CreateDb:
    def __init__(self, name=':memory:', path=''):
        self._name = name
        self._path = path
        self._connection = lite.connect(path + self._name)
        self.cursor = self._connection.cursor()

    def createTable(self, tablename='test', liste_champs=['champ_test']):
        str_liste_champs=",".join(liste_champs)
        self.cursor.execute(SQL_CREATE.format(table=tablename, fields=str_liste_champs))

    def insertIntoTable(self, tablename='test', values=[('record1',)]):
        str_nb_champs = ','.join('?'*len(values[0]))
        self.cursor.executemany(SQL_INSERT.format(table=tablename, values=str_nb_champs), values)

    def getDataFromTable(self, tablename='test'):
        self.cursor.execute("SELECT * FROM {}".format(tablename))
        rows = self.cursor.fetchall()
        return rows  # return a tuple sequence

    def printDataFromTable(self, tablename='test'):
        for row in db.getDataFromTable(tablename):
            print(",".join(row))

    def close(self):
        self._connection.close()


if __name__ == "__main__":
    try:
        # usage with default values
        db = CreateDb()
        db.createTable()
        db.insertIntoTable()
        records =[]
        records.append(('record2',))
        records.append(('record3',))
        db.insertIntoTable('test', records)
        db.printDataFromTable()

        # Usage with user-defined values
        db.createTable('client',('nom', 'prenom'))
        records = []
        records.append(('Jon','Doe'))
        records.append(('Jane', 'Jane'))
        db.insertIntoTable('client', records)
        db.printDataFromTable('client')
    finally:
        db.close()