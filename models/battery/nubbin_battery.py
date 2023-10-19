#!/usr/bin/python3
"""Defines the NubbinBattery class"""
from models.serviceable import Serviceable
from models.car import Car


class SpindlerBattery(Car, Serviceable):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def battery_should_be_serviced(self):
        if self.current_date > 4:
            return True
        else:
            return False
