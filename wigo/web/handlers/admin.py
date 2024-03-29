# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from flask import jsonify


def mont_routes_for_admin(app):
    @app.route('/ping')
    def ping():
        return jsonify(answer='pong')
