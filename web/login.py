#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get,	post, request   # or route

def check_login(user, passwd):
    pass

@post('/login')  # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username,	password):
        return "<p>Your	login	information	was	correct.</p>"
    else:
        return "<p>Login failed.</p>"

