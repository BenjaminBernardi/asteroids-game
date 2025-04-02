import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        if hasattr(self.__class__, 'containers'):
            for container in self.__class__.containers:
                container.add(self)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), self.radius)
