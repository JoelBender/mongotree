#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# read the README file
with open('README.rst') as readme_file:
    readme = readme_file.read()

# read the HISTORY file
with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

# read the module, extract the metadata
with open('mongotree.py') as module_file:
    metadata = dict(
        re.findall(
            "__([a-z]+)__ = '([^']+)'",
            module_file.read(),
        ))

requirements = [
    'pymongo',
]

setup_requirements = [
    'pytest-runner',
    ]

test_requirements = [
    'pytest',
    'bacpypes',
]

import mongotree

setup(
    name='mongotree',
    version=metadata['version'],
    description="Python module for tree structures in MongoDB",
    long_description=readme + '\n\n' + history,
    author=metadata['author'],
    author_email=metadata['email'],
    url='https://github.com/JoelBender/mongotree',
    py_modules=[
        'mongotree'
    ],
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='mongotree',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    setup_requires=setup_requirements,

    test_suite='tests',
    tests_require=test_requirements
)
