SYSUBBS API Server
------------------

.. image:: https://travis-ci.org/zonyitoo/sysubbs-apiserver.png?branch=master   
    :target: https://travis-ci.org/zonyitoo/sysubbs-apiserver

http://bbs.sysu.edu.cn

Note: *Still developing. Don't panic. Current version is not ready for public use.*

Dependences
===========

Python dependences are defined in ``requirements.txt``. And it also depend on **Redis** server.

Deployment
==========

Example on **Ubuntu 13.10 amd64**.

.. code:: bash

    $ sudo apt-get update && sudo apt-get install redis-server python-virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ cd server
    $ python app.py

TODOs
=====

* Backend processors with **jsbbs** APIs' support. (Current)

* Backend processors that using databases directly.
