# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

#
# Error
#

class Error(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return message


#
# Flask-based Web Application
#

def build_app():
    from wigo.data.cassandra import Database
    from wigo.data.store import StateMachine

    from flask import Flask, request, jsonify, Response
    
    #
    # Settings
    #

    app = Flask(__name__)
    app.config.from_object('wigo.config.DefaultSettings')
    app.config.from_envvar('WIGO_SETTINGS', silent=True)

    #: Need to think on a better place to do it
    Database.setup(app.config['CASSANDRA_URI'])


    #
    # Error handling
    #

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(message="Not Found", url=request.url), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify(message="Internal Server Error", url=request.url), 500


    #
    # Filtering
    #

    @app.before_request
    def before_request():
        pass


    #
    # API Request Handling
    #

    @app.route('/ping')
    def ping():
        return jsonify(answer='pong')


    @app.route('/statemachines', methods=['POST'])
    def new_state_machine():
        app.logger.info(request.data)

        payload = request.json

        state_machine = StateMachine(metadata=payload)
        state_machine.register_new()

        response = Response('', status=201, mimetype='application/json')
        response.headers['Location'] = '/statemachines/%s' % state_machine.Name

        return response

    return app
