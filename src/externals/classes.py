import pygame
from src.externals.cfg import *
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('src/Char.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.hitbox = pygame.Rect(0, 0, 12, 12)

        self.rect = self.image.get_rect(center=(640, 360))

    def update(self):
        self.hitbox.center = self.rect.center

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # self.metadata = metadata
        self.image = pygame.Surface((150, 150))
        self.image.fill((255, 255, 0))
        # self.image.fill(metadata["colour"])

        self.rect = self.image.get_rect(center=(640, 100))

class Boss_Mod(pygame.sprite.Sprite):
    def __init__(self, metadata):
        super().__init__()

        self.metadata = metadata
        self.image = pygame.Surface((150, 150))
        self.image.fill(metadata["colour"])

        self.rect = self.image.get_rect(center=(640, 100))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()

        # self.image = pygame.Surface((20, 20))
        self.image = pygame.image.load('src/bullet.png').convert_alpha()
        # self.image.fill((120, 120, 255))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class BossBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()

        self.image = pygame.image.load('src/Boss bullet A.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class BossBulletCurve(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y, turn_speed=1):
        super().__init__()

        self.image = pygame.image.load('src/Boss bullet A.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed_x = speed_x
        self.speed_y = speed_y
        self.turn_speed = math.radians(turn_speed)

    def update(self):
        old_x = self.speed_x
        old_y = self.speed_y

        self.speed_x = (
            old_x * math.cos(self.turn_speed) - old_y * math.sin(self.turn_speed)
        )

        self.speed_y = (
            old_x * math.sin(self.turn_speed) + old_y * math.cos(self.turn_speed)
        )

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.radius = 200
        self.duration = BOMB_DURATION # ms
        self.start_time = pygame.time.get_ticks()

        diameter = self.radius * 2

        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)

        pygame.draw.circle(self.image, (255, 255, 0, 70), (self.radius, self.radius), self.radius, 4)

        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        current_time = pygame.time.get_ticks()

        for bullet in active_boss_bullets:
            distance = math.dist(self.rect.center, bullet.rect.center)

            if distance <= self.radius:
                bullet.kill()

        # End bomb
        if current_time - self.start_time >= self.duration:
            self.kill()