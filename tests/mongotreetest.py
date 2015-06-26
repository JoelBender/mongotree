#!/usr/bin/python

"""
MongoTreeTest

This module contains the base class for developing a test
fixture for MongoTree tests.
"""

import os
import sys

from bacpypes.debugging import bacpypes_debugging, ModuleLogger
from bacpypes.consolelogging import ArgumentParser

import pymongo
from mongotree import MongoTree

# some debugging
_debug = 0
_log = ModuleLogger(globals())

# database pieces
test_host = None
test_connection = None
test_database = None
test_collection = None
test_flush = False
test_dump = False


#
#   setUpPackage
#


@bacpypes_debugging
def setUpPackage():
    global test_host, test_connection, test_database, test_collection, \
        test_flush, test_dump

    # create an argument parser
    parser = ArgumentParser(description=__doc__)

    # add an option to select the host
    parser.add_argument('--host', help="connect to a host",
                        default=os.getenv("MONGOTREE_HOST") or "localhost",
                        )

    # add an option to select the database
    parser.add_argument('--db', help="database",
                        default=os.getenv("MONGOTREE_DB") or "test",
                        )

    # add an option to select the collection
    parser.add_argument('--collection', help="collection",
                        default=os.getenv("MONGOTREE_COLLECTION") or "mongotree",
                        )

    # add a flush option
    parser.add_argument('--flush',
                        help="flush the collection before running test",
                        action='store_true', default=True,
                        )

    # add a dump option
    parser.add_argument('--dump',
                        help="dump the collection after running test",
                        action='store_true', default=True,
                        )

    # get the debugging args and parse them
    arg_str = os.getenv("MONGOTREE_DEBUG") or ""
    test_args = parser.parse_args(arg_str.split())

    if _debug: setUpPackage._debug("setUpPackage")
    if _debug: setUpPackage._debug("    - test_args: %r", test_args)

    # save the host
    test_host = test_args.host
    if _debug: setUpPackage._debug("    - test_host: %r", test_host)

    # create a connection
    test_connection = pymongo.MongoClient(test_args.host)
    if _debug: setUpPackage._debug("    - test_connection: %r", test_connection)

    # reference a database
    test_database = test_connection[test_args.db]
    if _debug: setUpPackage._debug("    - test_database: %r", test_database)

    # reference a collection
    test_collection = test_database[test_args.collection]
    if _debug: setUpPackage._debug("    - test_collection: %r", test_collection)

    # flush before each case
    test_flush = test_args.flush
    if _debug: setUpPackage._debug("    - test_flush: %r", test_flush)

    # dump after each case
    test_dump = test_args.dump
    if _debug: setUpPackage._debug("    - test_dump: %r", test_dump)


#
#   tearDownPackage
#


@bacpypes_debugging
def tearDownPackage():
    if _debug: tearDownPackage._debug("tearDownPackage")
    global test_connection

    # close the connection
    test_connection.close()


#
#   MongoTreeTestContext
#


@bacpypes_debugging
class MongoTreeTestContext(MongoTree):

    def __init__(self, collection=None, marshal=None):
        if _debug: MongoTreeTestContext._debug("__init__ %r", marshal)

        # provide a default collection
        if collection is None:
            collection = test_collection

        # continue initializing a tree
        MongoTree.__init__(self, collection, marshal)

    def setUp(self, flush=None):
        if _debug: MongoTreeTestContext._debug("setUp %r", flush)
        global test_flush

        # check for local override
        if flush is None:
            flush = test_flush

        # flush first
        if flush:
            stats = self.collection.remove()
            if _debug: MongoTreeTestContext._debug("    - flush stats: %r", stats)
        else:
            if _debug: MongoTreeTestContext._debug("    - no flush")

        # easier method chaining
        return self

    def tearDown(self, dump=None):
        if _debug: MongoTreeTestContext._debug("tearDown %r", dump)
        global test_dump

        # check for parameter override
        if dump is None:
            dump = test_dump

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
