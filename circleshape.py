import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # will use this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classses must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def collision_checker(self, object):
        r1 = self.radius
        r2 = object.radius

        distance = pygame.math.Vector2.distance_to(self.position, object.position)
        return distance <= r1 + r2 