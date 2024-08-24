from Config import Config
from LifeEngine import LifeEngine
import random
import math


class PhysicsEngine:
    def __init__(self, config: Config):
        self.config = config
        self.bodies = list(self.initialize_bodies())

    def initialize_bodies(self):
        raise NotImplementedError(
            "This method should be overridden in subclasses")

    def apply_physics(self):
        raise NotImplementedError(
            "This method should be overridden in subclasses")


class CosmicPhysicsEngine(PhysicsEngine):
    def initialize_bodies(self):
        for _ in range(self.config.num_bodies):
            yield {
                "type": "Celestial Body",
                "mass": 1.0,
                "vx": random.uniform(-1, 1),
                "vy": random.uniform(-1, 1),
                "x": random.uniform(0, 800),
                "y": random.uniform(0, 600)
            }

    def apply_physics(self):
        for body in self.bodies:
            # Simple example: gravitational attraction to a point (400, 300)
            center_x, center_y = 400, 300
            dx = center_x - body['x']
            dy = center_y - body['y']
            distance = math.sqrt(dx**2 + dy**2)
            force = self.config.gravitational_constant * \
                body['mass'] / (distance**2)
            body['vx'] += force * dx / distance
            body['vy'] += force * dy / distance
            body['x'] += body['vx']
            body['y'] += body['vy']


class MicrobialPhysicsEngine(PhysicsEngine):
    def initialize_bodies(self):
        print("Initializing microbial bodies...")
        for _ in range(self.config.initial_population):
            yield {
                "type": "Microbe",
                "age": 0,
                "alive": True,
                "growth_rate": self.config.growth_rate,
                "x": random.uniform(0, 800),
                "y": random.uniform(0, 600)
            }

    def apply_physics(self):
        life_engine = LifeEngine(self.bodies, resources=100)
        life_engine.apply_life_cycle()


class AtomicPhysicsEngine(PhysicsEngine):
    def initialize_bodies(self):
        for _ in range(self.config.num_bodies):
            yield {
                "type": "Atom",
                "charge": 1.0,
                "vx": random.uniform(-1, 1),
                "vy": random.uniform(-1, 1),
                "x": random.uniform(0, 800),
                "y": random.uniform(0, 600)
            }

    def apply_physics(self):
        for body in self.bodies:
            # Example: Coulomb force interaction between charged partdricles
            for other_body in self.bodies:
                if other_body is not body:
                    dx = other_body['x'] - body['x']
                    dy = other_body['y'] - body['y']
                    distance = math.sqrt(dx**2 + dy**2)
                    if distance > 0:
                        force = (body['charge'] *
                                 other_body['charge']) / (distance**2)
                        body['vx'] += force * dx / distance
                        body['vy'] += force * dy / distance
            body['x'] += body['vx']
            body['y'] += body['vy']
