#!/usr/bin/python3
"""Defines the Thovex class"""
from datetime import datetime
from models.battery.nubbin_battery import NubbinBattery
from models.engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


class Thovex(NubbinBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.now().date() or self.battery_should_be_serviced():
            return True
        else:
            return False
