#!/usr/bin/python3
"""Defines the test class module NubbinBattery"""
import unittest
from datetime import date
from models.battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2023-10-29")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_not_service(self):
        current_date = date.fromisoformat("2023-10-29")
        last_service_date = date.fromisoformat("2022-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
