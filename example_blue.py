# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:20:34 2023

@author: nabet
"""

from flask import Blueprint
example_blue=Blueprint('example_blue', __name__)



@example_blue.route('/')
def index():
    return '<h1>example app</h1>'