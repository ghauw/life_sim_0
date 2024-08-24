import json
import pygame
from Config import Config
from UniverseFactoryModule import UniverseFactoryModule
from PhysicsEngine import PhysicsEngine, CosmicPhysicsEngine, MicrobialPhysicsEngine, AtomicPhysicsEngine
from Renderer import Renderer
from LoggerEngine import Logger

# Load the configuration from the JSON file
with open('config.json', 'r') as file:
    config_data = json.load(file)

# Create Config objects based on the loaded JSON data
cosmic_config = Config(**config_data['cosmic'])
microbial_config = Config(**config_data['microbial'])
atomic_config = Config(**config_data['atomic'])
display_config = config_data['display']  # Load display configuration


def main(simulation_type_override=None):
    universe_factory = UniverseFactoryModule()

    # Screen setup based on config
    screen_width = display_config['screen_width']
    screen_height = display_config['screen_height']
    flags = pygame.FULLSCREEN if display_config['full_screen'] else 0
    window = pygame.display.set_mode((screen_width, screen_height), flags)

    # Set refresh rate and sleep time if configured
    refresh_rate = display_config['refresh_rate']
    sleep_time = display_config.get('sleep_time', 1.0 / refresh_rate)

    # Get the universe type from the user or override
    try:
        universe_type = simulation_type_override or input(
            "Enter the type of universe (Cosmic System, Microbial System, Atomic System) [default: Microbial System]: ").strip().lower()
        if not universe_type:
            universe_type = 'microbial system'
            print("Defaulting to Microbial System.")
    except ValueError as e:
        print(f"Error: {e}")
        return  # Exit if the universe type is invalid

    # Map universe type to the corresponding config and engine
    if universe_type == 'cosmic system':
        config = cosmic_config
        physics_engine = CosmicPhysicsEngine(config)
    elif universe_type == 'microbial system':
        config = microbial_config
        physics_engine = MicrobialPhysicsEngine(config)
    elif universe_type == 'atomic system':
        config = atomic_config
        physics_engine = AtomicPhysicsEngine(config)
    else:
        print("Unknown universe type. Defaulting to Microbial System.")
        config = microbial_config
        physics_engine = MicrobialPhysicsEngine(config)

    pygame.init()
    renderer = Renderer(window)
    logger = Logger(metrics_to_log=[
                    "time", "bodies", "live_microbes", "mean_velocity", "rms_velocity", "total_energy"])

    running = True
    while running:
        physics_engine.apply_physics()
        renderer.draw(physics_engine.bodies)
        logger.log(physics_engine)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        # Sleep to control frame rate
        pygame.time.delay(int(sleep_time * 1000))

    pygame.quit()


if __name__ == "__main__":
    main()
