#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mongotree
----------------------------------

Tests for `mongotree` module.
"""

import sys
import unittest

from bacpypes.debugging import bacpypes_debugging, ModuleLogger

# import conftest
from conftest import MongoTreeTestContext

# some debugging
_debug = 0
_log = ModuleLogger(globals())


@bacpypes_debugging
def test_fixture(db):
    if _debug: test_fixture._debug("test_fixture %r", db)


@bacpypes_debugging
def setup_module(module):
    if _debug: setup_module._debug("setup_module %r", module)

@bacpypes_debugging
def teardown_module(module):
    if _debug: teardown_module._debug("teardown_module %r", module)


@bacpypes_debugging
class TestMongotree(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        if _debug: TestMongotree._debug("setup_class %r", cls)

    @classmethod
    def teardown_class(cls):
        if _debug: TestMongotree._debug("teardown_class %r", cls)

    def setup_method(self, method):
        if _debug: TestMongotree._debug("setup_method %r %r", self, method)

    def teardown_method(self, method):
        if _debug: TestMongotree._debug("teardown_method %r %r", self, method)

    def test_something(self):
        if _debug: TestMongotree._debug("test_something")

    def test_something_else(self):
        if _debug: TestMongotree._debug("test_something_else")
