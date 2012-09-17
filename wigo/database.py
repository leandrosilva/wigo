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

from pycassa import ConnectionPool, ColumnFamily, NotFoundException
from pycassa.system_manager import SystemManager, SIMPLE_STRATEGY, UTF8_TYPE
from pycassa.cassandra.ttypes import InvalidRequestException

class Cassandra(object):
    __URI = None
    
    @classmethod
    def setup(clazz, CASSANDRA_URI):
        clazz.__URI = CASSANDRA_URI
        clazz.__create_schema()
            
    @classmethod
    def __create_schema(clazz):
        ERROR_KS_WIGO_ALREADY_EXISTS = 'Keyspace names must be case-insensitively unique ("wigo" conflicts with "wigo")'
        ERROR_CF_STATEMACHINES_ALREADY_EXISTS = "Cannot add already existing column family 'StateMachines' to keyspace 'wigo'."

        system_manager = clazz.new_system_manager()
        
        try:
            system_manager.create_keyspace('wigo', SIMPLE_STRATEGY, {'replication_factor': '1'})
        except InvalidRequestException as e:
            if e.why == ERROR_KS_WIGO_ALREADY_EXISTS:
                pass
            else:
                raise e

        try:
            system_manager.create_column_family('wigo', 'StateMachines', super=False, comparator_type=UTF8_TYPE)
        except InvalidRequestException as e:
            if e.why == ERROR_CF_STATEMACHINES_ALREADY_EXISTS:
                pass
            else:
                raise e
        
        system_manager.close()
    
    @classmethod
    def get_uri(clazz):
        return clazz.__URI
        
    @classmethod
    def new_system_manager(clazz):
        return SystemManager(clazz.__URI)
    
    @classmethod
    def new_connection_pool(clazz, keyspace):
        return ConnectionPool(keyspace, clazz.__URI)
