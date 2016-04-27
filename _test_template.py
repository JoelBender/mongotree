#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nose Test Module Template
-------------------------

This module is a template for creating MongoTree test cases.  To create a
module of new tests, make a copy of this template and rename the
TestCaseTemplate and associated test_something functions.

Before writing any tests, decide if you want a test tree to be module level
(shared by all of the tests in the module), class level (shared by the tests
in the class) or test level (a new tree created for each test).  Remove the
comments from the appropriate functions, and to help keep the module tidy,
remove the unnecessary functions and comments.

In following with the nose testing methodology, setUpModule() will be called
before all of the tests in this module, setUpClass() will be called before
all of the tests in the class, and setUp() will be called before each test.
Similarly, tearDown() will be called after each test, tearDownClass() will be
called after all of the tests in the class, and tearDownModule() will be
called after all of the classes in the module.
"""

import unittest

from mongotreetest import bacpypes_debugging, ModuleLogger
# from mongotest import MongoTreeTestContext

# some debugging
_debug = 0
_log = ModuleLogger(globals())


@bacpypes_debugging
def setUpModule():
    if _debug: setUpModule._debug("setUpModule")

    # create a module level test tree and set it up
    # global test_tree
    # test_tree = MongoTreeTestContext().setUp()


@bacpypes_debugging
def tearDownModule():
    if _debug: tearDownModule._debug("tearDownModule")

    # tear down the module level test tree
    # global test_tree
    # test_tree.tearDown()


@bacpypes_debugging
class TestCaseTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if _debug: TestCaseTemplate._debug("setUpClass")

        # create a class level test tree and set it up
        # cls.test_tree = MongoTreeTestContext().setUp()

    @classmethod
    def tearDownClass(cls):
        if _debug: TestCaseTemplate._debug("tearDownClass")

        # tear down the class level test tree
        # cls.test_tree.tearDown()

    def setUp(self):
        if _debug: TestCaseTemplate._debug("setUp")

        # create a test level test tree and set it up
        # self.test_tree = MongoTreeTestContext().setUp()

    def test_something(self):
        if _debug: TestCaseTemplate._debug("test_something")

    def test_something_else(self):
        if _debug: TestCaseTemplate._debug("test_something_else")

    def tearDown(self):
        if _debug: TestCaseTemplate._debug("tearDown")

        # tear down the test level test tree
        # self.test_tree.tearDown()
