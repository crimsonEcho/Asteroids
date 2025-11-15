from circleshape import *
from constants import *

class Shot(CircleShape):
    radius = SHOT_RADIUS
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS) #last argument is width

    def update(self, dt):
        self.position += self.velocity * dt