import random


class UniverseFactoryModule:
    def create_universe(self, universe_type):
        if universe_type == "Cosmic System":
            return {"universe_type": universe_type, "properties": self.create_cosmic_system()}
        elif universe_type == "Microbial System":
            return {"universe_type": universe_type, "properties": self.create_microbial_system()}
        elif universe_type == "Atomic System":
            return {"universe_type": universe_type, "properties": self.create_atomic_system()}
        else:
            return DefaultInputHandler().get_default_config()

    def create_cosmic_system(self):
        return {
            "num_bodies": self.get_valid_integer("Enter the number of celestial bodies (e.g., 50): ", default=50),
            "gravitational_constant": self.get_valid_float("Enter the gravitational constant (e.g., 6.67430e-11): ", default=6.67430e-11)
        }

    def create_microbial_system(self):
        return {
            "initial_population": self.get_valid_integer("Enter the initial population of microbes (e.g., 100): ", default=100),
            "growth_rate": self.get_valid_float("Enter the growth rate (e.g., 0.1): ", default=0.1),
            "reproduction_rate": self.get_valid_float("Enter the reproduction rate (e.g., 0.05): ", default=0.05),
            "death_rate": self.get_valid_float("Enter the death rate (e.g., 0.02): ", default=0.02)
        }

    def create_atomic_system(self):
        return {
            "num_bodies": self.get_valid_integer("Enter the number of atoms (e.g., 100): ", default=100),
            "charge_interaction": self.get_valid_float("Enter the charge interaction factor (e.g., 1.0): ", default=1.0)
        }

    def get_valid_integer(self, prompt, default):
        try:
            value = int(input(prompt))
            return value if value > 0 else default
        except ValueError:
            return default

    def get_valid_float(self, prompt, default):
        try:
            value = float(input(prompt))
            return value if value > 0 else default
        except ValueError:
            return default


class SimulationConfig:
    def __init__(self):
        self.universe_type = self.get_universe_type()
        self.properties = UniverseFactoryModule().create_universe(
            self.universe_type)  # Removed extra argument

    def get_universe_type(self):
        # Randomly select a universe type
        universe_types = ["Cosmic System", "Microbial System", "Atomic System"]
        return random.choice(universe_types)
