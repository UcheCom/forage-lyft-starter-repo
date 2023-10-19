#!/usr/bin/python3
"""Defines the CapuletEngine class"""
from models.serviceable import Serviceable
from models.car import Car


class CapuletEngine(Car, Serviceable):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000