#!/usr/bin/python3
"""Defines the test class module for CarriganTire"""

import unittest
from models.tire.carrigan_tire import CarriganTire


class CarriganTire(unittest.TestCase):
    def test_needs_service(self):
        tire_wear_array = True
        tire = CarriganTire("tire_wear_array")
        self.assertTrue(tire.needs_service())

    def test_needs_service(self):
        tire_wear_array = False
        tire = CarriganTire("tire_wear_array")
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
