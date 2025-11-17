from circleshape import CircleShape
import constants
import pygame


class Shot(CircleShape):
    radius = constants.SHOT_RADIUS
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, constants.SHOT_RAD)

    def update(self, dt):
        self.position += self.velocity * dt