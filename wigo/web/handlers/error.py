# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from flask import request, jsonify


def mont_routes_for_error(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify(message="Not Found", url=request.url), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify(message="Internal Server Error", url=request.url), 500
