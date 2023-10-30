#!/usr/bin/python3
"""Defines the test class module for CarriganTires"""

import unittest
from models.tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear_array = [0.1, 0.3, 0.2, 0.9]
        tires = CarriganTires(tire_wear_array)
        self.assertTrue(tires.needs_service())

    def test_needs_not_service(self):
        tire_wear_array = [0.2, 0.3, 0.5, 0.6]
        tires = CarriganTires(tire_wear_array)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
