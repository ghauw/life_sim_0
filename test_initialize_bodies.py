from Config import Config
from PhysicsEngine import CosmicPhysicsEngine, MicrobialPhysicsEngine, AtomicPhysicsEngine


def test_initialize_bodies():
    # Test CosmicPhysicsEngine
    cosmic_config = Config(num_bodies=10, universe_type="Cosmic System")
    cosmic_engine = CosmicPhysicsEngine(cosmic_config)
    print("Testing CosmicPhysicsEngine...")
    for body in cosmic_engine.bodies:
        assert body["type"] == "Celestial Body"
        assert isinstance(body["mass"], float)
        assert isinstance(body["vx"], float)
        assert isinstance(body["vy"], float)
        assert isinstance(body["x"], float)
        assert isinstance(body["y"], float)
        print(body)

    # Test MicrobialPhysicsEngine
    microbial_config = Config(
        initial_population=5, growth_rate=0.1, universe_type="Microbial System")
    microbial_engine = MicrobialPhysicsEngine(microbial_config)
    print("\nTesting MicrobialPhysicsEngine...")
    for body in microbial_engine.bodies:
        assert body["type"] == "Microbe"
        assert isinstance(body["age"], int)
        assert isinstance(body["alive"], bool)
        assert isinstance(body["growth_rate"], float)
        assert isinstance(body["x"], float)
        assert isinstance(body["y"], float)
        print(body)

    # Test AtomicPhysicsEngine
    atomic_config = Config(num_bodies=8, universe_type="Atomic System")
    atomic_engine = AtomicPhysicsEngine(atomic_config)
    print("\nTesting AtomicPhysicsEngine...")
    for body in atomic_engine.bodies:
        assert body["type"] == "Atom"
        assert isinstance(body["charge"], float)
        assert isinstance(body["vx"], float)
        assert isinstance(body["vy"], float)
        assert isinstance(body["x"], float)
        assert isinstance(body["y"], float)
        print(body)


if __name__ == "__main__":
    test_initialize_bodies()
