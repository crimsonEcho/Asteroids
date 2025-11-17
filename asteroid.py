from circleshape import CircleShape
from constants import SPCROCK_MIN_RAD
from logger import log_event
import random
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= SPCROCK_MIN_RAD:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_vector_a = self.velocity.rotate(angle)
            new_vector_b = self.velocity.rotate(-angle)
            new_asteroid_a = Asteroid(
                self.position.x, self.position.y, self.radius - SPCROCK_MIN_RAD
                )
            new_asteroid_b = Asteroid(
                self.position.x, self.position.y, self.radius - SPCROCK_MIN_RAD
                )
            new_asteroid_a.velocity = new_vector_a * 1.2
            new_asteroid_b.velocity = new_vector_b * 1.2
