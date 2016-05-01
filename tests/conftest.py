#!/usr/bin/python

"""
Glue routines to simulate package setup and teardown.
"""

from .utilities import setup_package, teardown_package

#
#   pytest_configure
#

def pytest_configure(config):
    setup_package()


#
#   pytest_unconfigure
#

def pytest_unconfigure():
    teardown_package()