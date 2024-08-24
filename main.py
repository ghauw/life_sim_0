import pygame
from SimulationConfig import SimulationConfig
from PhysicsEngine import PhysicsEngine
from Renderer import Renderer
from LoggerEngine import Logger


def main():
    config = SimulationConfig()
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    physics_engine = PhysicsEngine(config.properties)
    renderer = Renderer(window)
    logger = Logger(metrics_to_log=["time", "bodies", "live_microbes"])

    running = True
    while running:
        physics_engine.apply_physics()
        renderer.draw(physics_engine.bodies)
        logger.log(physics_engine)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
