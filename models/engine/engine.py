#!/usr/bin/python3
"""Defines the Engine class."""
from abc import ABC


class Engine(ABC):
    def needs_service(self):
        pass
