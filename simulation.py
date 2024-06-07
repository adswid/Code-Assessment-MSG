from datetime import datetime, timedelta
from time import sleep


class Simulation:
    def __init__(self, time_step):
        self._participants = []
        self._time_step = time_step

    def add_participant(self, participant):
        self._participants.append(participant)

    def update(self):
        for participant in self._participants:
            participant.update()

    def run(self, duration_seconds):
        start_time = datetime.now()
        while datetime.now() - start_time <= timedelta(seconds=duration_seconds):
            self.update()
            sleep(self._time_step)