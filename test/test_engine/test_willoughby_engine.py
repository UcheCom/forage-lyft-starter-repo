#!/usr/bin/python3
"""Defines the test class module for WilloughbyEngine"""

import unittest
from models.engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_not_service(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
