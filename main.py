import csv


class Radar:
    def __init__(self, filename):
        self.datafile = open(filename, newline='')
        self.reader = csv.reader(self.datafile, delimiter=';')

    def scan_for_threats(self):
        try:
            return [int(value, 2) for value in next(self.reader)]
        except StopIteration:
            return None     # TODO print no data available


def main():
    radar = Radar('radar_data.csv')
    for i in range(100):
        print(radar.scan_for_threats())


if __name__ == "__main__":
    main()
