import pygame
import random
from src.externals.characterinit import *

# Game idea: Doubled Down
# Concept: A game where you have to dodge incoming drone attacks. Use your dodging skills to evade the bullets!
# Inspiration: Touhou franchise / Bullet hell

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doubled Down - ver. 1.0")
clock = pygame.time.Clock()

game_state = 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()

        self.image = pygame.Surface((20, 20))
        self.image.fill((120, 120, 255))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('/Volumes/Xylvera/coding/doubled-down/src/player (1).png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect(center=(640, 360))
player = Player()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((150, 150))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect(center=(640, 100))

active_bullets = pygame.sprite.Group()
BULLET_DELAY = 50 # milliseconds
last_shot = 0

boss = Boss()

# player = pygame.image.load('/Volumes/Xylvera/coding/doubled-down/src/character.png').convert_alpha()
# player = pygame.transform.scale(player, (1080, 1350))

font = pygame.font.Font(None, 50)

level = font.render("Level: Front gate", True, color=(255, 255, 255))
game_over = font.render("Game Over.", True, color=(255, 255, 255))

CEN = (640, 360)

level_rect = level.get_rect()
level_rect.topleft = (0, 0)
game_rect = game_over.get_rect()
game_rect.center = CEN

player_vel = 5

screen_rect = window.get_rect()
player.rect.clamp_ip(screen_rect)

while True:
    
    player_vel_x = 0
    player_vel_y = 0

    # Border check
    if player.rect.y >= 630:
        player.rect.y = 630
    if player.rect.x >= 1200:
        player.rect.x = 1200
    if player.rect.y <= 0:
        player.rect.y = 0
    if player.rect.x <= 0:
        player.rect.x = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_vel_x = -player_vel
    if keys[pygame.K_RIGHT]:
        player_vel_x = player_vel
    if keys[pygame.K_UP]:
        player_vel_y = -player_vel
    if keys[pygame.K_DOWN]:
        player_vel_y = player_vel
    if keys[pygame.K_z]:
        current_time = pygame.time.get_ticks()

        if current_time - last_shot >= BULLET_DELAY:
            add_bullet = Bullet(player.rect.centerx, player.rect.top, speed_x=0, speed_y=-20)
            active_bullets.add(add_bullet)

            last_shot = current_time

    if pygame.sprite.spritecollide(boss, active_bullets, True):
        print("hit")
        BOSS[0]["health"] -= 1

    print(keys[pygame.K_z])    
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)


    # if player_x >= 1280 or player_y >= 720:
    #     game_state = 2

    #     player_x, player_y = 1000, 1000
    #     player_vel_x, player_vel_y = 0, 0

    #     falling_object_x, falling_object_y = 1000, 1000
    #     falling_object_vel_x, falling_object_vel_y = 0, 0

    # if collision_detection():
        # falling_object_y = 0
        # falling_object_x = random.randint(0, window.width - 30)
    active_bullets.update()

    for bullet in active_bullets:
        if bullet.rect.bottom < 0 or bullet.rect.top > SCREEN_HEIGHT:
            bullet.kill()


    if game_state == 1:
        # falling_object_x += falling_object_vel_x
        # falling_object_y += falling_object_vel_y
        bhealth = font.render(f"Boss Health: {BOSS[0]["health"]}", True, color=(255, 255, 255))
        bhealth_rect = bhealth.get_rect()
        bhealth_rect.topleft = (0, 60)
        bombs_left = font.render(f"Bombs: {PLR["bombs"]}", True, (255, 255, 255))
        bombs_rect = bombs_left.get_rect()
        bombs_rect.topleft = (0, 120)
        stars = font.render(f"Stars: {PLR["stars"]}", True, (255, 255, 255))
        stars_rect = stars.get_rect()
        stars_rect.topleft = (0, 180)
        player.rect.x += player_vel_x
        player.rect.y += player_vel_y
        window.blit(player.image, player.rect)
        window.blit(boss.image, boss.rect )
        window.blit(level, level_rect)
        window.blit(bhealth, bhealth_rect)
        window.blit(bombs_left, bombs_rect)
        window.blit(stars, stars_rect)
        # window.blit(falling_object, (falling_object_x, falling_object_y))
    
    elif game_state == 2:
        pygame.display.set_caption("Game over!")
        window.blit(game_over, game_over.get_rect())

    pygame.display.flip()
    
    print(player.rect.x, player.rect.y, game_state)
    window.fill((0, 0, 0))
    active_bullets.draw(window)

    clock.tick(120)