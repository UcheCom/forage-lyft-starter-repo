#!/usr/bin/python3
"""Defines the Glissade class"""
from datetime import datetime
from models.battery.spindler_battery import SpindlerBattery
from models.engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


class Glissade(SpindlerBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.now().date() or self.battery_should_be_serviced():
            return True
        else:
            return False
