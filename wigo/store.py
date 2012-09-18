# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from wigo.core import Error
from wigo.cassandra import Database, Session

#
# Error
#

class MetadataError(Error):
    pass
    
class StoringError(Error):
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
    
    def register_new(self):
        with Database.open_session() as session:
            state_machines_column_family = session.get_column_family('StateMachines')
            
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
