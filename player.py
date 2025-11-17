from circleshape import CircleShape
from shot import Shot
import pygame
import constants


class Player(CircleShape):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius
                 / 1.5)
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = self.rotation + constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RAD)
        shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)
                         * constants.PLAYER_SHOOT_SPEED)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer > 0:
                return None
            else:
                self.shot_cooldown_timer = constants.PLAYER_SHT_COOLDOWN_SCNDS
                self.shoot()
