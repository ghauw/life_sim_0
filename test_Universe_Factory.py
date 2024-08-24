import UniverseFactoryModule as UF


def test_universe_factory():
    universe_factory = UF.UniverseFactoryModule()

    # Test Cosmic System
    cosmic_config = universe_factory.create_universe("Cosmic System")
    assert cosmic_config.universe_type == "Cosmic System"
    assert cosmic_config.num_bodies == 50  # Assuming default value
    assert cosmic_config.gravitational_constant == 6.67430e-11

    # Test Microbial System
    microbial_config = universe_factory.create_universe("Microbial System")
    assert microbial_config.universe_type == "Microbial System"
    assert microbial_config.initial_population == 100  # Assuming default value
    assert microbial_config.growth_rate == 0.1

    # Test Atomic System
    atomic_config = universe_factory.create_universe("Atomic System")
    assert atomic_config.universe_type == "Atomic System"
    assert atomic_config.num_bodies == 100  # Assuming default value
    assert atomic_config.charge_interaction == 1.0

    print("All tests passed!")


# Run the test
test_universe_factory()
