# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

class Settings:
    DEBUG = False
    TESTING = False
    CASSANDRA_URI = None
    
    @classmethod
    def reset(clazz, settings):
        clazz.DEBUG = settings['DEBUG']
        clazz.TESTING = settings['TESTING']
        clazz.CASSANDRA_URI = settings['CASSANDRA_URI']
    
class DefaultSettings(Settings):
    DEBUG = True
    CASSANDRA_URI = '127.0.0.1:9160'
