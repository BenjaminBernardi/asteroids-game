import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "cyan", self.triangle(), width=2)
        # pygame.draw.circle(screen, "red", self.position, self.radius, width=1)

    def update(self, dt):
        pass

    def check_collisions(self, another_circle):
        distance = self.position.distance_to(another_circle.position)
        return distance <= self.radius + another_circle.radius