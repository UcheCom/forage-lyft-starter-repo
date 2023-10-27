#!/usr/bin/python3
"""Defines the NubbinBattery class"""
from models.battery.battery import Battery
from models.utils import add_years_to_date


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self):
        date_battery_be_serviced = add_years_to_date(self.last_service_date, 4)
        if date_battery_be_serviced < self.current_date:
            return True
        else:
            return False
