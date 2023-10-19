#!/usr/bin/python3
"""Defines the Calliope class"""
from datetime import datetime
from models.battery.splindle_battery import SplindlerBattery
from models.engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


class Calliope(SpindlerBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.now().date() or self.battery_should_be_serviced():
            return True
        else:
            return False
