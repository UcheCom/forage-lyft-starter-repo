#!/usr/bin/python3
"""Defines the OctoprimeTire class"""
from models.tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        if sum(tire_wear_array) >= 3:
            return True
        else:
            return False
