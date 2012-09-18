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
    
class MetadataError(Error):
    pass
    
#
# Model
#

class State(object):
    def __init__(self, metadata):
        self.__metadata = metadata
        self.__validate()
        
        self.Name = metadata['name']
        
        if 'next' in metadata:
            self.Next = metadata['next']
        else:
            self.Next = None
    
    def __validate(self):
        if not 'name' in self.__metadata:
            raise MetadataError('States should have a name.')

class StateMachine(object):
    def __init__(self, metadata):
        self.__metadata = metadata
        self.__validate()
        
        self.Name = metadata['name']
        self.States = self.__build_states()
    
    def __validate(self):
        if not 'name' in self.__metadata:
            raise MetadataError('State machines should have a name.')
        
        if not 'states' in self.__metadata:
            raise MetadataError('State machines should have at least one state.')
    
    def __build_states(self):
        states_metadata = self.__metadata['states']
        
        return [State(state_metadata) for state_metadata in states_metadata]
    
    def __get_column_name(self):
        return 'SM_%s' % self.Name
        
    def register_new(self):
        return self.Name
