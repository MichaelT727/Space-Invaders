import pygame
from spaceship import SpaceShip
from aliens import Aliens, alienProjectile
import random

screen_width = 800
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

pygame.display.set_caption("Space Defenders")
bg = pygame.image.load("space_background.jpg")

pygame.init()


class Game:
    def __init__(self):
        spaceship = SpaceShip((screen_width / 2, screen_height), screen_width, screen_height / 1.35)
        self.spaceship = pygame.sprite.GroupSingle(spaceship)

        self.aliens = pygame.sprite.Group()

        self.alien_direction = 1

        self.alienProjectiles = pygame.sprite.Group()

    def spawn_aliens(self, rowOfAliens, colOfAliens):
        xOffset = screen_width / rowOfAliens
        yOffset = screen_height / 12

        for col in range(1, colOfAliens):
            for row in range(1, rowOfAliens):
                self.aliens.add(Aliens(xOffset * row, yOffset * col))

    def update_aliens(self):
        self.aliens.draw(screen)
        for aliens in self.aliens.sprites():
            aliens.move(self.alien_direction)

    def alien_border_check(self):
        for aliens in self.aliens.sprites():
            if aliens.rect.right >= screen_width:
                self.alien_direction = -1
                for aliens2 in self.aliens.sprites():
                    aliens2.descend()

            elif aliens.rect.left <= 0:
                self.alien_direction = 1
                for aliens3 in self.aliens.sprites():
                    aliens3.descend()

    def collision_check(self):
        for laser in self.spaceship.sprite.projectiles:
            for alien in self.aliens:
                if pygame.sprite.collide_rect(laser, alien):
                    laser.kill()
                    alien.kill()

    def alien_laser(self, alien):
        if alien.alienType == 1:
            self.alienProjectiles.add(alienProjectile(alien.rect.center, "red"))
        elif alien.alienType == 2:
            self.alienProjectiles.add(alienProjectile(alien.rect.center, "blue"))
        elif alien.alienType == 3:
            self.alienProjectiles.add(alienProjectile(alien.rect.center, "green"))

    def updateAlienProjectile(self):
        for laser in self.alienProjectiles:
            laser.rect.y += 3

    def run(self):
        self.spaceship.sprite.projectiles.draw(screen)
        self.spaceship.update()
        self.spaceship.draw(screen)

        self.update_aliens()
        self.alien_border_check()
        self.updateAlienProjectile()
        self.alienProjectiles.draw(screen)


health = 3

if __name__ == "__main__":
    game = Game()
    time = 0
    while health != 0:
        screen.blit(bg, (0, 0))

        # spawns aliens
        if len(game.aliens) == 0:
            game.spaceship.sprite.projectiles.empty()
            game.alienProjectiles.empty()
            game.spawn_aliens(8, 6)

        # alien projectile timer
        if time >= 3000:
            for alien in game.aliens:
                if random.randint(1, len(game.aliens) + 1) <= 3:
                    game.alien_laser(alien)
            time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                health = 0
            if event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE:
                game.spaceship.sprite.shootLaser()
                print(game.spaceship.sprite.projectiles)
                print(game.aliens)

        # alien laser projectile check
        for laser in game.alienProjectiles:
            if pygame.sprite.collide_rect(game.spaceship.sprite, laser):
                laser.kill()
                health -= 1
                print(health)

        game.collision_check()
        game.run()

        pygame.display.update()
        time += clock.tick(60)
