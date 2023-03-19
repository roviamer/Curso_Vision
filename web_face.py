# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:56:37 2023

@author: nabet
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hola </h1>'


