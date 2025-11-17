import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCRN_WD}")
    print(f"Screen height: {constants.SCRN_HT}")

    pygame.init()
    screen = pygame.display.set_mode(
        (constants.SCRN_WD, constants.SCRN_HT)
        )
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid = AsteroidField()
    player = Player(constants.SCRN_WD / 2, constants.SCRN_HT / 2)

    dt = 0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for obj in asteroids:
            if obj.collision_check(player):
                print("Game Over!")
                raise SystemExit
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
