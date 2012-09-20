# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

import sys, os.path

WIGO_LIB_DIR = os.path.abspath(os.path.dirname(__file__) + '/../../')
sys.path.insert(0, WIGO_LIB_DIR)


#: Web Application ~ Integration Tests


import unittest

from wigo.web import build_web_application

from flask import jsonify


class WebApplicationTestCase(unittest.TestCase):
    def __init__(self, test_function):
        unittest.TestCase.__init__(self, test_function)

        self.app = build_web_application().test_client()
        
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_ping(self):
        rv = self.app.get('/ping')
        assert rv.status == '200 OK'
        assert '"answer": "pong"' in rv.data
    
    def test_not_found(self):
        rv = self.app.get('/not/found')
        assert rv.status == '404 NOT FOUND'
        assert '"message": "Not Found"' in rv.data
        assert '"url": "http://localhost/not/found"' in rv.data


if __name__ == '__main__':    
    unittest.main()