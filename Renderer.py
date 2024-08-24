import pygame

class Renderer:
    def __init__(self, window):
        self.window = window

    def draw(self, bodies):
        self.window.fill((0, 0, 0))  # Clear the screen with black

        for body in bodies:
            if body['type'] == "Celestial Body":
                self.draw_celestial_body(body)
            elif body['type'] == "Microbe":
                self.draw_microbe(body)
            elif body['type'] == "Atom":
                self.draw_atom(body)

        pygame.display.flip()

    def draw_celestial_body(self, body):
        pygame.draw.circle(self.window, (255, 255, 255),
                           (int(body['x']), int(body['y'])), 5)

    def draw_microbe(self, body):
        pygame.draw.circle(self.window, (0, 255, 0),
                           (int(body['x']), int(body['y'])), 3)

    def draw_atom(self, body):
        pygame.draw.circle(self.window, (255, 0, 0),
                           (int(body['x']), int(body['y'])), 2)
