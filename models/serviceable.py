#!/usr/bin/python3
"""Defines the parent class for other classes."""

from abc import ABC, abstractmethod


class Serviceable(ABC):
    """This defines the seviceable class for car interface"""
    def __init__(self, last_service_date):
        """Initializes the Serviceable class"""
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass