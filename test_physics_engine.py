import unittest
from Config import Config
from PhysicsEngine import CosmicPhysicsEngine, MicrobialPhysicsEngine, AtomicPhysicsEngine


class TestPhysicsEngines(unittest.TestCase):
    def test_cosmic_physics_engine_initialization(self):
        config = Config(
            num_bodies=10, gravitational_constant=6.67430e-11, universe_type="Cosmic System")
        engine = CosmicPhysicsEngine(config)

        self.assertEqual(len(engine.bodies), 10)
        for body in engine.bodies:
            self.assertEqual(body['type'], "Celestial Body")
            self.assertTrue(0 <= body['x'] <= 800)
            self.assertTrue(0 <= body['y'] <= 600)

    def test_cosmic_physics_engine_apply_physics(self):
        config = Config(
            num_bodies=10, gravitational_constant=6.67430e-11, universe_type="Cosmic System")
        engine = CosmicPhysicsEngine(config)

        initial_positions = [(body['x'], body['y']) for body in engine.bodies]
        engine.apply_physics()
        new_positions = [(body['x'], body['y']) for body in engine.bodies]

        self.assertNotEqual(initial_positions, new_positions)

    def test_microbial_physics_engine_initialization(self):
        config = Config(initial_population=10, growth_rate=0.1, reproduction_rate=0.05,
                        death_rate=0.02, universe_type="Microbial System")
        engine = MicrobialPhysicsEngine(config)

        self.assertEqual(len(engine.bodies), 10)
        for body in engine.bodies:
            self.assertEqual(body['type'], "Microbe")
            self.assertTrue(0 <= body['x'] <= 800)
            self.assertTrue(0 <= body['y'] <= 600)

    def test_microbial_physics_engine_apply_physics(self):
        config = Config(initial_population=10, growth_rate=0.1, reproduction_rate=0.05,
                        death_rate=0.02, universe_type="Microbial System")
        engine = MicrobialPhysicsEngine(config)

        initial_population = len(engine.bodies)
        engine.apply_physics()
        new_population = len(engine.bodies)

        # Population should change due to life cycle
        self.assertNotEqual(initial_population, new_population)

    def test_atomic_physics_engine_initialization(self):
        config = Config(num_bodies=10, charge_interaction=1.0,
                        universe_type="Atomic System")
        engine = AtomicPhysicsEngine(config)

        self.assertEqual(len(engine.bodies), 10)
        for body in engine.bodies:
            self.assertEqual(body['type'], "Atom")
            self.assertTrue(0 <= body['x'] <= 800)
            self.assertTrue(0 <= body['y'] <= 600)

    def test_atomic_physics_engine_apply_physics(self):
        config = Config(num_bodies=10, charge_interaction=1.0,
                        universe_type="Atomic System")
        engine = AtomicPhysicsEngine(config)

        initial_positions = [(body['x'], body['y']) for body in engine.bodies]
        engine.apply_physics()
        new_positions = [(body['x'], body['y']) for body in engine.bodies]

        self.assertNotEqual(initial_positions, new_positions)


if __name__ == '__main__':
    unittest.main()
