# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

import wigo

from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash

app = Flask(__name__)
app.config.from_object('wigo.config.DefaultSettings')
app.config.from_envvar('WIGO_SETTINGS', silent=True)

@app.route('/')
def home():
    return render_template('home.html')

### Here we go!

if __name__ == '__main__':
    app.run()
