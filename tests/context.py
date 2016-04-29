#!/usr/bin/python

"""
MongoTree Test Context
"""

import os
import sys
import pytest
import pymongo
import unittest

from bacpypes.debugging import bacpypes_debugging, ModuleLogger
from bacpypes.consolelogging import ArgumentParser

from . import conftest
from mongotree import MongoTree

# some debugging
_debug = 0
_log = ModuleLogger(globals())


#
#   MongoTreeTestContext
#

@bacpypes_debugging
class MongoTreeTestContext(MongoTree):

    def __init__(self, collection=None, marshal=None):
        if _debug: MongoTreeTestContext._debug("__init__ %r", marshal)

        # provide a default collection
        if collection is None:
            collection = conftest.test_collection

        # continue initializing a tree
        MongoTree.__init__(self, collection, marshal)

    def setup_context(self, flush=None):
        if _debug: MongoTreeTestContext._debug("setup_context flush=%r", flush)

        # check for local override
        if flush is None:
            flush = conftest.test_flush

        # flush first
        if flush:
            stats = self.collection.remove()
            if _debug: MongoTreeTestContext._debug("    - flush stats: %r", stats)
        else:
            if _debug: MongoTreeTestContext._debug("    - no flush")

        # easier method chaining
        return self

    def teardown_context(self, dump=None):
        if _debug: MongoTreeTestContext._debug("teardown_context dump=%r", dump)

        # check for parameter override
        if dump is None:
            dump = conftest.test_dump

        # flush the cache
        self.flush_cache()

        # dump the contents
        if dump:
            for doc in self.collection.find():
                attrs_str = ''.join(
                    "        %s: %r,\n" % (attr_name, attr_value)
                    for attr_name, attr_value in doc['_attrs'].items()
                    )
                contents_str = ''.join(
                    "        %r,\n" % (node_id,)
                    for node_id in doc['_contents']
                    )
                sys.stdout.write("%r\n    attrs: {\n%s        },\n    contents: [\n%s        ]\n"
                                 % (doc['_id'], attrs_str, contents_str)
                                 )
        else:
            if _debug: MongoTreeTestContext._debug("    - no dump")

        # consistent method chaining
        return self


#
#   MongoTreeClassContext
#

@bacpypes_debugging
class MongoTreeClassContext(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        if _debug: MongoTreeClassContext._debug("setup_class %r", cls)

        cls.context = MongoTreeTestContext()
        cls.context.setup_context()

    @classmethod
    def teardown_class(cls):
        if _debug: MongoTreeClassContext._debug("teardown_class %r", cls)

        cls.context.teardown_context()
        cls.context = None


#
#   MongoTreeMethodContext
#

@bacpypes_debugging
class MongoTreeMethodContext(unittest.TestCase):

    def setup_method(self, method):
        if _debug: MongoTreeMethodContext._debug("setup_method %r %r", self, method)

        # set up a context for this instance
        self.context = MongoTreeTestContext()
        self.context.setup_context()

    def teardown_method(self, method):
        if _debug: MongoTreeMethodContext._debug("teardown_method %r %r", self, method)

        # tear down the context
        self.context.teardown_context()
        self.context = None
