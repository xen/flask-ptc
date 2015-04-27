#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.app_name }}
----------------------------------

Tests for `{{ cookiecutter.app_name }}` module.
"""

import unittest

from {{ cookiecutter.app_name }} import {{ cookiecutter.app_name }}


class Test{{ cookiecutter.app_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
