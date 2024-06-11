import logging
from collections import Counter
from random import random
import csv

logger = logging.getLogger(__name__)


class Radar:
    def __init__(self, filename):
        """Mock of the Radar system, which obtains its data from a CSV file.

        Parameters
        ----------
        filename: str
            Path to the csv file containing radar data
        """
        self.datafile = open(filename, newline='')
        self.reader = csv.reader(self.datafile, delimiter=';')

    def scan_for_threats(self):
        """Get a single radar scan.

        Returns
        -------
        list of str
            A single radar measurement, containing a list of binary numbers in text form.

        """
        try:
            return next(self.reader)
        except StopIteration:
            return None


class IFF:
    """Identification Friend or Foe system mock."""

    @staticmethod
    def check_for_hostile_entity(radar_data):
        """Check radar data for existence of hostiles.

        The hostile entry is found when there are more odd values
        in the radar measurement.

        Parameters
        ----------
        radar_data: list of str
             A single radar measurement, containing a list of binary numbers in text form.

        Returns
        -------
        bool
            True, if the hostile has been identified; false if not.
        """
        # To checking for parity in binary we just need to look at the last digit
        counter = Counter(value[-1] for value in radar_data)
        return counter['1'] > counter['0']


class FiringUnit:
    def __init__(self, probability_of_kill):
        """Firing unit with a customizable probability of kill.

        Parameters
        ----------
        probability_of_kill: float
            Change of successful engagement.
        """
        self._probability_of_kill = probability_of_kill

    def fire_missile(self):
        """Fires missile and evaluates the result.

        Returns
        -------
        bool
            True, if the enemy was successfully eliminated; otherwise False.
        """
        return random() <= self._probability_of_kill


class PatriotSystem:
    def __init__(self, radar_data_source, probability_of_kill):
        """Patriot Air Defence System mock.

        Consists of a Radar, IFF and Firing Units

        Parameters
        ----------
        radar_data_source: str
            Path to the csv file containing radar data
        probability_of_kill: float
            Change of successful engagement.
        """
        self._radar = Radar(radar_data_source)
        self._iff = IFF()
        self._firing_unit = FiringUnit(probability_of_kill)

    def update(self):
        """Update the state of the system

        First, the system obtains the radar measurement.
        Next, it checks if any hostiles were detected.
        If so, it fires missiles and informs if the engagement was successful.

        Returns
        -------
        None
        """
        logger.info('Scanning for threats...')
        radar_data = self._radar.scan_for_threats()
        if not radar_data:
            logger.error('No radar data available')
            return
        logger.info('Checking for hostile entities...')
        if not self._iff.check_for_hostile_entity(radar_data):
            logger.info('Not hostiles identified.')
            return
        logger.info('Hostile identified! Firing missiles...')
        if self._firing_unit.fire_missile():
            logger.info('Target successfully neutralized!')
        else:
            logger.info('Target not neutralized.')
