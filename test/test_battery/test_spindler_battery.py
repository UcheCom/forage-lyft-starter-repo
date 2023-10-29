#!/usr/bin/python3
"""Defines the test class module for Spindlerbattery"""

import unittest
from datetime import date
from models.battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2023-10-28")
        last_service_date = date.fromisoformat("2021-06-30")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_not_service(self):
        current_date = date.fromisoformat("2023-10-28")
        last_service_date = date.fromisoformat("2022-06-15")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
