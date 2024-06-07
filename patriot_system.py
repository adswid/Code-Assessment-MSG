import logging
from random import random
import csv

logger = logging.getLogger(__name__)


class Radar:
    def __init__(self, filename):
        self.datafile = open(filename, newline='')
        self.reader = csv.reader(self.datafile, delimiter=';')

    def scan_for_threats(self):
        try:
            return [int(value, 2) for value in next(self.reader)]
        except StopIteration:
            logger.error("No radar data available")
            return None


class IFF:
    def check_for_hostile_entity(self, radar_data):
        odd_value_count = sum(value % 2 for value in radar_data)
        even_value_count = len(radar_data) - odd_value_count
        return odd_value_count > even_value_count


class FiringUnit:
    def __init__(self, probability_of_kill):
        self._probability_of_kill = probability_of_kill

    def fire_missile(self):
        # TODO seed generator
        return random() <= self._probability_of_kill


class PatriotSystem:
    def __init__(self):
        # TODO get parameters from ctr arguments
        self._radar = Radar('radar_data.csv')
        self._iff = IFF()
        self._firing_unit = FiringUnit(0.8)

    def update(self):
        logger.info("Scanning for threats...")
        radar_data = self._radar.scan_for_threats()
        if not radar_data:
            logger.error("No radar data available")
        logger.info("Checking for hostile entities...")
        if not self._iff.check_for_hostile_entity(radar_data):
            logger.info("Not hostiles identified.")
            return
        logger.info("Hostile identified! Firing missiles.")
        if self._firing_unit.fire_missile():
            logger.info("Target successfully neutralized!")
        else:
            logger.info("Target not neutralized.")
