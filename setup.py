#!/usr/bin/env python
import importlib
import os
import sys
import warnings

from setuptools import setup

if sys.version_info[0:2] < (3, 7):
    warnings.warn('This package is tested with Python version 3.7+', stacklevel=1)

root_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root_path, 'README.rst')) as readme:
    README = readme.read()

package_info = importlib.import_module('bankline_parser')

setup(
    name='bankline-direct-parser',
    version=package_info.__version__,
    author=package_info.__author__,
    author_email='dev@digital.justice.gov.uk',
    url='https://github.com/ministryofjustice/bankline-direct-parser',
    packages=['bankline_parser', 'bankline_parser.data_services'],
    include_package_data=True,
    license='MIT',
    description='Parser for Bankline Direct banking information services',
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',  # looser requirement than what's tested
    install_requires=[],
    tests_require=[],
    test_suite='tests',
)
