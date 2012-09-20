# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from wigo.data.cassandra import Database
from wigo.web.handlers.error import build_routes_for_error
from wigo.web.handlers.admin import build_routes_for_admin
from wigo.web.handlers.statemachines import build_routes_for_statemachines

from flask import Flask, request, jsonify, Response


def build_application():
    #: Settings

    app = Flask(__name__)
    app.config.from_object('wigo.config.DefaultSettings')
    app.config.from_envvar('WIGO_SETTINGS', silent=True)

    Database.setup(app.config['CASSANDRA_URI'])

    #: API Request Handling

    build_routes_for_error(app)
    build_routes_for_admin(app)
    build_routes_for_statemachines(app)

    #: DONE
    return app
