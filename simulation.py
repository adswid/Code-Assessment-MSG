from datetime import datetime, timedelta
from time import sleep


class Simulation:
    def __init__(self, time_step):
        """A quasi real-time simulation environment.

        When run, time simulation will call the `update` method of its participants with a given interval.

        Parameters
        ----------
        time_step : float
            Interval, in seconds, with which the participants' states will be updated

        """
        self._participants = []
        self._time_step = time_step

    def add_participant(self, participant):
        """Add participant to the simulation environment.

        Parameters
        ----------
        participant: Any
            Any object supporting the `update()` method

        Returns
        -------
        None
        """
        self._participants.append(participant)

    def update(self):
        """Update states of the participants."""
        for participant in self._participants:
            participant.update()

    def run(self, duration_seconds):
        """Run simulation in real-time for a given period.

        Parameters
        ----------
        duration_seconds: float
            Simulation duration in seconds

        Returns
        -------
        None
        """
        run_start_time = datetime.now()
        while True:
            step_start_time = datetime.now()
            if step_start_time - run_start_time > timedelta(seconds=duration_seconds):
                break
            self.update()
            # Try to compensate a bit for the duration of the update step
            sleep(self._time_step - (datetime.now()-step_start_time).seconds)
