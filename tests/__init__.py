#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing MongoTree
-----------------

This package contains the test applications for MongoTree.  The
`mongotreetest` module is used by the other test modules to use
a common testing environment, for example, they all reference
the same MongoDB database and collection.

The database connection/collection parameters can be specified
as environment variables or override by CLI options.
"""

from . import mongotreetest

from . import test_1

def setUpPackage():
    mongotreetest.setUpPackage()


def tearDownPackage():
    mongotreetest.tearDownPackage()
