#!/usr/bin/python3
"""This is the carfactory class module"""

from models.tire.carrigan_tire import CarriganTire
from models.tire.octoprime_tire import OctoprimeTire
from models.battery.nubbin_battery import NubbinBattery
from models.battery.spindler_battery import SpindlerBattery
from models.car import Car
from models.engine.capulet_engine import CapuletEngine
from models.engine.sternman_engine import SternmanEngine
from models.engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        tire = CarriganTire(tire_wear_array)
        tire = OctoprimeTire(tire_wear_array)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        tire = CarriganTire(tire_wear_array)
        tire = OctoprimeTire(tire_wear_array)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        tire = CarriganTire(tire_wear_array)
        tire = OctoprimeTire(tire_wear_array)
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        tire = CarriganTire(tire_wear_array)
        tire = OctoprimeTire(tire_wear_array)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        tire = CarriganTire(tire_wear_array)
        tire = OctoprimeTire(tire_wear_array)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
