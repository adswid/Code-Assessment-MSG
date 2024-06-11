import logging
import random
import os

from simulation import Simulation
from patriot_system import PatriotSystem


def main():
    script_path = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(format='[%(asctime)s]: %(message)s', level=logging.DEBUG)
    random.seed(0)      # Seed simulation for repeatability
    sim = Simulation(1.0)
    sim.add_participant(PatriotSystem(os.path.join(script_path, 'radar_data.csv'), 0.8))
    sim.run(20.0)


if __name__ == "__main__":
    main()
