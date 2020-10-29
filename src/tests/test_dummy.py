"""Test for unittest and main."""

import unittest
from main import add


class dummytest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
