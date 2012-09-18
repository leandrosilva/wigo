# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from pycassa import ConnectionPool, ColumnFamily, NotFoundException
from pycassa.system_manager import SystemManager, SIMPLE_STRATEGY, UTF8_TYPE
from pycassa.cassandra.ttypes import InvalidRequestException

class Database(object):
    __URI = None
    
    @classmethod
    def setup(clazz, CASSANDRA_URI):
        clazz.__URI = CASSANDRA_URI
        
        with Database.open() as database:
            database.__init_schema()
    
    @classmethod
    def open(clazz):
        return Database(SystemManager(clazz.__URI))
    
    @classmethod
    def open_session(clazz):
        return Session(ConnectionPool('wigo', server_list=[clazz.__URI]))
    
    def __init__(self, system_manager):
        self.__system_manager = system_manager
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.close()
    
    def close(self):
        self.__system_manager.close()
    
    def __init_schema(self):
        self.__create_keyspace()
        self.__create_column_families()
    
    def __create_keyspace(self):
        ERROR_KS_ALREADY_EXISTS = 'Keyspace names must be case-insensitively unique ("wigo" conflicts with "wigo")'

        try:
            self.__system_manager.create_keyspace('wigo', SIMPLE_STRATEGY, {'replication_factor': '1'})
        except InvalidRequestException as e:
            if e.why == ERROR_KS_ALREADY_EXISTS:
                pass
            else:
                raise e
    
    def __create_column_family(self, name, comparator_type=UTF8_TYPE):
        ERROR_CF_ALREADY_EXISTS = "Cannot add already existing column family '%s' to keyspace 'wigo'." % name

        try:
            self.__system_manager.create_column_family('wigo', name, super=False, comparator_type=comparator_type)
        except InvalidRequestException as e:
            if e.why == ERROR_CF_ALREADY_EXISTS:
                pass
            else:
                raise e
    
    def __create_column_families(self):
        self.__create_column_family('StateMachines')
        
class Session(object):
    def __init__(self, connection_pool):
        self.__connection_pool = connection_pool
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.close()
    
    def get_column_family(self, name):
        return ColumnFamily(self.__connection_pool, name)
    
    def close(self):
        self.__connection_pool.dispose()
