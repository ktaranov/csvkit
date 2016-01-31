#!/usr/bin/env python

import sys

import six

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

from csvkit.utilities.csvstat import CSVStat, launch_new_instance
from tests.utils import CSVKitTestCase, ColumnsTests, NamesTests


class TestCSVStat(CSVKitTestCase, ColumnsTests, NamesTests):
    Utility = CSVStat

    def test_launch_new_instance(self):
        with patch.object(sys, 'argv', ['csvstat', 'examples/dummy.csv']):
            launch_new_instance()

    def test_runs(self):
        self.get_output(['examples/test_utf8.csv'])

    def test_encoding(self):
        self.get_output(['-e', 'latin1', 'examples/test_latin1.csv'])

    def test_no_header_row(self):
        output = self.get_output(['-H', '-c', '2', 'examples/no_header_row.csv'])
        self.assertFalse('A' in output)
        self.assertTrue('B' in output)

    def test_count_only(self):
        output = self.get_output(['--count', 'examples/dummy.csv'])
        self.assertEqual(output, 'Row count: 1\n')
