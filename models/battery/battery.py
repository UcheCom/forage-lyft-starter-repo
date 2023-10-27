#!/usr/bin/python3
"""Defines the Battery class"""
from abc import ABC


class Battery(ABC):
    def needs_service(self):
        pass
