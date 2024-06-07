import csv
from random import  random

class Radar:
    def __init__(self, filename):
        self.datafile = open(filename, newline='')
        self.reader = csv.reader(self.datafile, delimiter=';')

    def scan_for_threats(self):
        try:
            return [int(value, 2) for value in next(self.reader)]
        except StopIteration:
            return None  # TODO print no data available


class IFF:
    def check_for_hostile_entity(self, radar_data):
        odd_value_count = sum(value % 2 for value in radar_data)
        even_value_count = len(radar_data) - odd_value_count
        return odd_value_count > even_value_count


class FiringUnit:
    def __init__(self, probability_of_kill):
        self._probability_of_kill = probability_of_kill

    def fire_missile(self):
        return random() <= self._probability_of_kill


def main():
    radar = Radar('radar_data.csv')
    iff = IFF()
    firing_unit = FiringUnit(0.8)
    while True:
        radar_data = radar.scan_for_threats()
        if radar_data is None:
            break
        if iff.check_for_hostile_entity(radar_data):
            print(firing_unit.fire_missile())


if __name__ == "__main__":
    main()
