#!/usr/bin/python3
"""Defines the car class module"""

from models.serviceable import Serviceable


class Car(Serviceable):
    """class car inherits from Serviceable"""
    def __init__(self, engine, battery, tire):
        self.tire = tire
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
