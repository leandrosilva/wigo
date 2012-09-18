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
        system_manager = clazz.new_system_manager()
        clazz.__create_wigo_keyspace(system_manager)
        clazz.__create_statemachines_column_family(system_manager)
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
    
    @classmethod
    def create_column_family(clazz, system_manager, name, comparator_type=UTF8_TYPE):
        ERROR_CF_ALREADY_EXISTS = "Cannot add already existing column family '%s' to keyspace 'wigo'." % name

        try:
            system_manager.create_column_family('wigo', name, super=False, comparator_type=comparator_type)
        except InvalidRequestException as e:
            if e.why == ERROR_CF_ALREADY_EXISTS:
                pass
            else:
                raise e
    
    @classmethod
    def __create_wigo_keyspace(clazz, system_manager):
        ERROR_KS_ALREADY_EXISTS = 'Keyspace names must be case-insensitively unique ("wigo" conflicts with "wigo")'
        
        try:
            system_manager.create_keyspace('wigo', SIMPLE_STRATEGY, {'replication_factor': '1'})
        except InvalidRequestException as e:
            if e.why == ERROR_KS_ALREADY_EXISTS:
                pass
            else:
                raise e

    @classmethod
    def __create_statemachines_column_family(clazz, system_manager):
        clazz.create_column_family(system_manager, 'StateMachines')
