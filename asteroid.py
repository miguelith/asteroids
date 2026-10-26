import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            rand = random.uniform(20, 50)

            asteroid_1 = Asteroid(
                self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS
            )
            asteroid_2 = Asteroid(
                self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS
            )

            asteroid_1.velocity = self.velocity.rotate(rand) * 1.2
            asteroid_2.velocity = self.velocity.rotate(-rand) * 1.2
