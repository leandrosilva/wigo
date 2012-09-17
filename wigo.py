# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from wigo.core import Initializer
from wigo.model import StateMachine

from flask import Flask, request, session, url_for, redirect, render_template, \
                  abort, g, flash, jsonify, Response

#
# Settings
#

app = Flask(__name__)
app.config.from_object('wigo.config.DefaultSettings')
app.config.from_envvar('WIGO_SETTINGS', silent=True)

Initializer.boot_for(app)

#
# Error handling
#

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

#
# Filtering
#

@app.before_request
def before_request():
    pass

#
# General
#

@app.route('/')
def home():
    return redirect(url_for('dashboard_index'))

#
# Dashboard
#

@app.route('/dashboard')
def dashboard_index():
    return render_template('dashboard/index.html')

#
# API
#

@app.route('/api/ping')
def api_ping():
    return jsonify(result='pong')

@app.route('/api/statemachines', methods=['POST'])
def api_new_state_machine():
    app.logger.info(request.data)

    payload = request.json
    
    state_machine = StateMachine(metadata=payload)
    state_machine.register_new()
    
    response = Response('', status=201, mimetype='application/json')
    response.headers['Location'] = '/api/statemachines/%s' % state_machine.Name
    
    return response

#
# Here we go!
#

if __name__ == '__main__':
    app.run()
