# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from wigo.cassandra import Database, Session

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

class StateMachine(object):
    def __init__(self, metadata):
        self.__validate(metadata)
        
        self.Name = metadata['name']
        self.States = self.__build_states(metadata['states'])
    
    def __validate(self, metadata):
        if not 'name' in metadata:
            raise MetadataError('State machines should have a name.')
        
        if not 'states' in metadata:
            raise MetadataError('State machines should have at least one state.')
    
    def __build_states(self, states_metadata):
        return [State(state_metadata) for state_metadata in states_metadata]
    
    def __get_column_name(self):
        return 'SM_%s' % self.Name
        
    def register_new(self):
        return self.Name
    
class State(object):
    def __init__(self, metadata):
        self.__validate(metadata)
        
        self.Name = metadata['name']
        
        if 'next' in metadata:
            self.Next = metadata['next']
        else:
            self.Next = None
    
    def __validate(self, metadata):
        if not 'name' in metadata:
            raise MetadataError('States should have a name.')
