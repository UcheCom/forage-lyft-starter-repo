#!/usr/bin/python3
"""Defines the test class module for OctoprimeTires"""

import unittest
from models.tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear_array = [0.9, 0.6, 0.7, 0.9]
        tires = OctoprimeTires(tire_wear_array)
        self.assertTrue(tires.needs_service())

    def test_needs_not_service(self):
        tire_wear_array = [0.3, 0.4, 0.2, 0.5]
        tires = OctoprimeTires(tire_wear_array)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
