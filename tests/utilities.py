#!/usr/bin/python

"""
"""

import os
import sys
import pytest
import pymongo

import pymongo.periodic_executor

from bacpypes.debugging import bacpypes_debugging, ModuleLogger
from bacpypes.consolelogging import ArgumentParser

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
#   setup_package
#

@bacpypes_debugging
def setup_package():
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

    if _debug: setup_package._debug("setup_package")
    if _debug: setup_package._debug("    - test_args: %r", test_args)

    # save the host
    test_host = test_args.host
    if _debug: setup_package._debug("    - test_host: %r", test_host)

    # create a connection
    test_connection = pymongo.MongoClient(test_args.host)
    if _debug: setup_package._debug("    - test_connection: %r", test_connection)

    # reference a database
    test_database = test_connection[test_args.db]
    if _debug: setup_package._debug("    - test_database: %r", test_database)

    # reference a collection
    test_collection = test_database[test_args.collection]
    if _debug: setup_package._debug("    - test_collection: %r", test_collection)

    # flush before each case
    test_flush = test_args.flush
    if _debug: setup_package._debug("    - test_flush: %r", test_flush)

    # dump after each case
    test_dump = test_args.dump
    if _debug: setup_package._debug("    - test_dump: %r", test_dump)

    if _debug: setup_package._debug("    - periodic executors: %r", pymongo.periodic_executor._EXECUTORS)


@bacpypes_debugging
def teardown_package():
    if _debug: teardown_package._debug("teardown_package")
    global test_connection

    # close the connection
    test_connection.close()
    if _debug: teardown_package._debug("    - connection closed")

    if _debug: teardown_package._debug("    - periodic executors: %r", pymongo.periodic_executor._EXECUTORS)
