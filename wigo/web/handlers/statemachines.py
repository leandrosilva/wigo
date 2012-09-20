# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from wigo.data.store import StateMachine

from flask import request, Response, jsonify


def build_routes_for_statemachines(app):
    @app.route('/statemachines', methods=['POST'])
    def new_state_machine():
        app.logger.info(request.data)

        payload = request.json

        state_machine = StateMachine(metadata=payload)
        state_machine.register_new()

        response = Response('', status=201, mimetype='application/json')
        response.headers['Location'] = '/statemachines/%s' % state_machine.Name

        return response
