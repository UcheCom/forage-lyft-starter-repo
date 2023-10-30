#!/usr/bin/python3
"""Defines the OctoprimeTires class"""
from models.tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        if sum(self.tire_wear_array) >= 3.0:
            return True
        else:
            return False
