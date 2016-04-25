#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mongotree
----------------------------------

Tests for `mongotree` module.
"""

import unittest

from .mongotreetest import bacpypes_debugging, ModuleLogger, MongoTreeTestContext

# some debugging
_debug = 0
_log = ModuleLogger(globals())


@bacpypes_debugging
class TestMongotree(unittest.TestCase):

    def setUp(self):
        if _debug: TestMongotree._debug("setUp")

        # create a test level test tree and set it up
        self.test_tree = MongoTreeTestContext().setUp()
        if _debug: TestMongotree._debug("    - test_tree: %r", self.test_tree)

    def test_something(self):
        if _debug: TestMongotree._debug("test_something")

    def tearDown(self):
        if _debug: TestMongotree._debug("tearDown")

        # tear down the test level test tree
        self.test_tree.tearDown()
