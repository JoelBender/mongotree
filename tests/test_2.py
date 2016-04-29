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

from .context import MongoTreeMethodContext

# some debugging
_debug = 0
_log = ModuleLogger(globals())


@bacpypes_debugging
class TestMongotree(MongoTreeMethodContext):

    def test_something(self):
        if _debug: TestMongotree._debug("test_something [context=%r]", self.context)

    def test_something_else(self):
        if _debug: TestMongotree._debug("test_something_else [context=%r]", self.context)
