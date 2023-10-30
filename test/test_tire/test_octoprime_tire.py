#!/usr/bin/python3
"""Defines the test class module for OctoprimeTire"""

import unittest
from models.tire.octoprime_tire import OctoprimeTire


class OctoprimeTire(unittest.TestCase):
    def test_needs_service(self):
        tire_wear_array = True
        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service(self):
        tire_wear_array = False
        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
