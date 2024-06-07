from simulation import Simulation
from patriot_system import PatriotSystem
import logging

def main():
    logging.basicConfig(format='[%(asctime)s]: %(message)s', level=logging.DEBUG)
    sim = Simulation(1.0)
    sim.add_participant(PatriotSystem())
    sim.run(20.0)


if __name__ == "__main__":
    main()
