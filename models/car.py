#!/usr/bin/python3
"""Defines the car class module"""

from models.serviceable import Serviceable


class Car(Serviceable):
    """class car inherits from Serviceable"""
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass
