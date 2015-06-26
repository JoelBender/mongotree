#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'pymongo'
]

test_requirements = [
    'bacpypes'
]

import mongotree

setup(
    name='mongotree',
    version=mongotree.__version__,
    description="Python module for tree structures in MongoDB",
    long_description=readme + '\n\n' + history,
    author=mongotree.__author__,
    author_email=mongotree.__email__,
    url='https://github.com/JoelBender/mongotree',
    py_modules=[
        'mongotree'
    ],
#    packages=[
#        'mongotree',
#    ],
#    package_dir={'mongotree':
#                 'mongotree'},
#    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='mongotree',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
