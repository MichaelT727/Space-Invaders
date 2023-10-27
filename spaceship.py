import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, pos, x_constraint, y_constraint):
        super().__init__()
        self.image = pygame.image.load("spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (pos[1] / 10, pos[1] / 10))
        self.rect = self.image.get_rect(midbottom=pos)

        self.pos = pos
        self.x_constraint = x_constraint
        self.y_constraint = y_constraint

        self.speed = 5

        self.projectiles = pygame.sprite.Group()

    def getInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def constraints(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.x_constraint:
            self.rect.right = self.x_constraint

        if self.rect.top <= self.y_constraint:
            self.rect.top = self.y_constraint
        if self.rect.bottom >= self.pos[1]:
            self.rect.bottom = self.pos[1]

    def shootLaser(self):
        self.projectiles.add(SpaceShipProjectile(self.rect.center))


    def update(self):
        self.getInput()
        self.constraints()
        for lasers in self.projectiles:
            lasers.rect.y -= self.speed
            if lasers.rect.y <= -10:
                lasers.kill()
class SpaceShipProjectile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((10, 40))
        self.image.fill("green")
        self.rect = self.image.get_rect(center=pos)






