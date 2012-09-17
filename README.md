# wigo

Wigo stands for **What is going on?**

This is an application and API to keep track on state machines, which is quite useful
for monitoring and metrics.

## Getting Started

* TODO

### Requirements

* [**Cassandra**](http://wiki.apache.org/cassandra/GettingStarted) up and running
* [**Flask**](http://flask.pocoo.org) and [**PyCassa**](https://github.com/pycassa/pycassa) libraries installed

### Installation and running

    $ git clone https://github.com/leandrosilva/wigo.git
    $ cd wigo
    $ python wigo.py

### Configuration

You can override **wigo** default settings, whose which should never be used on production environment, by follow these two simple steps:

1º. Create a configuration file with new settings:

    # /etc/wigo/production.config
	
	DEBUG = False
	TESTING = False
	CASSANDRA_URI = 'production.cassandra.wigo:9160'

2º. Set an environment variable pointing to that file:

	$ WIGO_SETTINGS=/etc/wigo/production.config python wigo.py

Of course, you might create different settings for each environment you target to run it, e.g. test, systems integration.

## Documentation

* [API](https://github.com/leandrosilva/wigo/blob/master/docs/APIDOC.md)
* Dashboard

## License

This software is licensed under the MIT license.

Copyright (c) 2012 Leandro Silva (CødeZøne) <leandrodoze@gmail.com>.
