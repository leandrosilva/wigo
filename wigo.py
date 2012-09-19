# -*- coding: utf-8 -*-
"""
    Wigo - What is going on?
    ~~~~~~~~~~~~~~~~~~~~~~~~

    An application and API to keep track on state machines. It's quite useful
    for monitoring and metrics.

    :copyright: (c) 2012 by Leandro Silva ~ CodeZone.
    :license: MIT.
"""

from wigo.core import build_app


#
# Here we go!
#

if __name__ == '__main__':
    app = build_app()
    app.run()
