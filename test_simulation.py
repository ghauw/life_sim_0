import random
import pygame
from main import main as run_simulation
from SimulationConfig import SimulationConfig, UniverseFactory


def run_simulations(num_iterations=100, log_file='simulation_logs.txt'):
    for i in range(4):  # Four different test runs
        print(f"Running iteration {i+1}/{4} with seed {i}...")
        random.seed(i)
        run_simulation()
        # Collect logs and data here if needed


if __name__ == "__main__":
    run_simulations()
