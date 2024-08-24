from UniverseFactoryModule import UniverseFactoryModule
from PhysicsEngine import PhysicsEngine
from main import main


def run_simulations():
    # Test with different simulation types
    simulation_types = ["Cosmic System", "Microbial System", "Atomic System"]

    for sim_type in simulation_types:
        print(f"Running simulation for {sim_type}...")
        main(simulation_type_override=sim_type)


if __name__ == "__main__":
    run_simulations()
