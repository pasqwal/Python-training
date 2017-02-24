#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://apprendre-python.com/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite
# https://fr.wikibooks.org/wiki/Apprendre_%C3%A0_programmer_avec_Python/Gestion_d'une_base_de_donn%C3%A9es

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)