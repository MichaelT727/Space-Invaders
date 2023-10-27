import pygame
import random


class Aliens(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.alienType = random.randint(1,3)
        self.image = pygame.Surface((60, 60))

        if self.alienType == 1:
            self.image = pygame.image.load("aliens/red_alien.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (60,60))
        elif self.alienType == 2:
            self.image = pygame.image.load("aliens/blue_alien.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 60))
        elif self.alienType == 3:
            self.image = pygame.image.load("aliens/green_alien.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect(center = (x, y))

        self.xspeed = 1
        self.yspeed = 2

        self.alienProjectiles = pygame.sprite.Group()

    def move(self, direction):
        self.rect.x += (direction * self.xspeed)

    def descend(self):
        self.rect.y += self.yspeed

class alienProjectile(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        self.image = pygame.Surface((10, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)





