from LifeEngine import LifeEngine  # Ensure this import is present

class PhysicsEngine:
    def __init__(self, config):
        self.config = config
        self.bodies = self.initialize_bodies()

    def initialize_bodies(self):
        bodies = []
        if self.config['universe_type'] == "Cosmic System":
            bodies = self.create_cosmic_bodies(self.config['properties']['num_bodies'])
        elif self.config['universe_type'] == "Microbial System":
            bodies = self.create_microbes(self.config['properties']['initial_population'])
        elif self.config['universe_type'] == "Atomic System":
            bodies = self.create_atoms(self.config['properties']['num_bodies'])
        return bodies

    def create_cosmic_bodies(self, num_bodies):
        return [{"type": "Celestial Body", "mass": 1.0, "velocity": 0, "position": (0, 0)} for _ in range(num_bodies)]

    def create_microbes(self, initial_population):
        return [{"type": "Microbe", "age": 0, "alive": True, "growth_rate": self.config['properties']['growth_rate']} for _ in range(initial_population)]

    def create_atoms(self, num_atoms):
        return [{"type": "Atom", "charge": 1.0, "velocity": 0, "position": (0, 0)} for _ in range(num_atoms)]

    def apply_physics(self):
        if self.config['universe_type'] == "Cosmic System":
            self.apply_cosmic_physics()
        elif self.config['universe_type'] == "Microbial System":
            self.apply_microbial_physics()
        elif self.config['universe_type'] == "Atomic System":
            self.apply_atomic_physics()

    def apply_cosmic_physics(self):
        for body in self.bodies:
            # Enhanced gravitational interaction
            body['velocity'] += body['mass'] * 0.01  # Simplified example

    def apply_microbial_physics(self):
        life_engine = LifeEngine(self.bodies, resources=100)  # Make sure LifeEngine is imported and used correctly
        life_engine.apply_life_cycle()

    def apply_atomic_physics(self):
        for body in self.bodies:
            body['velocity'] += body['charge'] * 0.01  # Simplified charge interaction
