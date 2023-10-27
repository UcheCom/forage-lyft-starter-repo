#!/usr/bin/python3
"""Defines the parent class for other classes."""

from abc import ABC, abstractmethod


class Serviceable(ABC):
    """This defines the seviceable class for car interface."""

    @abstractmethod
    def needs_service(self):
        pass
