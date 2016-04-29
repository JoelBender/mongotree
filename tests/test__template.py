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

# some debugging
_debug = 0
_log = ModuleLogger(globals())


#
#   Module Setup and Teardown
#

@bacpypes_debugging
def setup_module(module):
    if _debug: setup_module._debug("setup_module %r", module)

@bacpypes_debugging
def teardown_module(module):
    if _debug: teardown_module._debug("teardown_module %r", module)


#
#   Function Testing Setup and Teardown
#

@bacpypes_debugging
def setup_function(function):
    if _debug: setup_function._debug("setup_function %r", function)

@bacpypes_debugging
def teardown_function(function):
    if _debug: teardown_function._debug("teardown_function %r", function)


#
#   Test Function
#

@bacpypes_debugging
def test_something():
    if _debug: test_something._debug("test_something")

#
#   Test Class Template
#

@bacpypes_debugging
class TestClass(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        if _debug: TestClass._debug("setup_class %r", cls)

    @classmethod
    def teardown_class(cls):
        if _debug: TestClass._debug("teardown_class %r", cls)

    def setup_method(self, method):
        if _debug: TestClass._debug("setup_method %r %r", self, method)

    def teardown_method(self, method):
        if _debug: TestClass._debug("teardown_method %r %r", self, method)

    def test_something(self):
        if _debug: TestClass._debug("test_something")

    def test_something_else(self):
        if _debug: TestClass._debug("test_something_else")
