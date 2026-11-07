import pygame
from src.externals.cfg import *
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(resource_path('src/Char.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.hitbox = pygame.Rect(0, 0, 12, 12)

        self.rect = self.image.get_rect(center=(640, 360))

    def update(self):
        self.hitbox.center = self.rect.center

class BossHealthBar:
    def __init__(self, x, y, w, h, hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.current = hp

    def draw(self, surface):
        ratio = self.current / self.hp
        current_width = int(self.w * ratio)

        bg_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        hp_rect = pygame.Rect(self.x, self.y, current_width, self.h)

        pygame.draw.rect(surface, colour["white"], bg_rect)
        pygame.draw.rect(surface, colour["red"], hp_rect)


# class BossHealthbar(pygame.Surface):
#     def __init__(self):
#         super().__init__()

#         self.image = pygame.Surface((240, 50))
#         self.image = self.image.fill(colour["white"])

#     def update(self):
#         self.image = pygame.transform.scale(())

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # self.metadata = metadata
        self.image = pygame.Surface((150, 150))
        # self.image = pygame.image.load('src/messi.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        # self.image.fill((255, 255, 0))
        # self.image.fill(metadata["colour"])

        self.rect = self.image.get_rect(center=(640, 100))

class Boss_Mod(pygame.sprite.Sprite):
    def __init__(self, metadata):
        super().__init__()

        self.metadata = metadata
        # self.image = pygame.Surface((150, 150))
        self.image = pygame.image.load(resource_path(metadata['decals']))
        self.image = pygame.transform.scale(self.image, (128, 128))
        # self.image.fill(metadata["colour"])

        self.rect = self.image.get_rect(center=(640, 100))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()

        # self.image = pygame.Surface((20, 20))
        self.image = pygame.image.load(resource_path('src/Bullet (1).png')).convert_alpha()
        # self.image.fill((120, 120, 255))
        self.image = pygame.transform.scale(self.image, (10, 50))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class BossBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()

        self.image = pygame.image.load(resource_path('src/Boss bullet A.png')).convert_alpha()
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

        self.image = pygame.image.load(resource_path('src/Boss bullet A.png')).convert_alpha()
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

class Points(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y):
        super().__init__()
        self.image = pygame.image.load(resource_path('src/points.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.x = x
        self.y = y

        self.rect = self.image.get_rect(center=(x, y))


        self.vel_x = vel_x
        self.vel_y = vel_y

    def home_to_player(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        distance = math.hypot(dx, dy)

        if distance < 10:
            PLR["score"] += 12500
            self.kill()
            return

        speed = 12
        self.rect.x += (dx / distance) * speed
        self.rect.y += (dy / distance) * speed

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Lives(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y):
        super().__init__()
        self.image = pygame.image.load(resource_path('src/lives.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.x = x
        self.y = y

        self.rect = self.image.get_rect(center=(x, y))


        self.vel_x = vel_x
        self.vel_y = vel_y

    def home_to_player(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        distance = math.hypot(dx, dy)

        if distance < 10:
            PLR["lives"] += 1
            self.kill()
            return

        speed = 12
        self.rect.x += (dx / distance) * speed
        self.rect.y += (dy / distance) * speed

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class Firepower(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y):
        super().__init__()
        self.image = pygame.image.load(resource_path('src/Firepower_upgrade.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.x = x
        self.y = y

        self.rect = self.image.get_rect(center=(x, y))


        self.vel_x = vel_x
        self.vel_y = vel_y

    def home_to_player(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        distance = math.hypot(dx, dy)

        if distance < 10:
            PLR["firepower_addition"] += 1
            self.kill()
            return

        speed = 12
        self.rect.x += (dx / distance) * speed
        self.rect.y += (dy / distance) * speed

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y