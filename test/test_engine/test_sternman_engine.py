#!/usr/bin/python3
"""Defines the test class module for SternmanEngine"""

import unittest
from models.engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
