#!/usr/bin/python3
"""Defines the CarriganTire class"""
from models.tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        if any(wear >= 0.9 for wear in tire_wear_array):
            return True
        else:
            return False
