# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from wigo.config import Settings
from wigo.database import Cassandra

#
# Error
#

class Error(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return message
