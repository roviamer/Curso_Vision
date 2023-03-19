# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:24:30 2023

@author: nabet
"""

from flask import Flask
from example_blue import example_blue


app=Flask(__name__)
app.register_blueprint(example_blue)

if __name__=='__main__':
    app.run()