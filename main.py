import pygame
import random
import math
from src.externals.classes import *
from src.externals.characterinit import *
from src.externals.functions import *
from src.externals.cfg import *

# Game idea: Doubled Down
# Concept: A game where you have to dodge incoming drone attacks. Use your dodging skills to evade the bullets!
# Inspiration: Touhou franchise / Bullet hell

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("Native Faith.mp3")

pygame.mixer.music.set_volume(.4)

pygame.mixer.music.play(1)


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doubled Down - ver. 1.0")
clock = pygame.time.Clock()

game_state = 1

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

player = Player()

# Player's bullet
BULLET_DELAY = 100 # milliseconds
last_shot = 0

# Boss' bullet
BOSS_SHOOT_DELAY = 120 # ms
boss_last_shot = 0

IMMUNITY_PERIOD = 1500 # ms
immunity_latest = 0


boss = Boss()

font = pygame.font.Font(None, 50)

level = font.render("Level: Front gate", True, color=(255, 255, 255))
game_over = font.render("Game Over.", True, color=(255, 255, 255))

level_rect = level.get_rect()
level_rect.topleft = (0, 0)
game_rect = game_over.get_rect()
game_rect.center = CEN

player_vel = 5

screen_rect = window.get_rect()
player.rect.clamp_ip(screen_rect)

rotation = 0


while True:
    current_time = get_current_time()
    # fix players vel to 0 every frame with no keyboard input.
    player_vel_x = 0
    player_vel_y = 0

    player_vel = 5

    # Border check
    keys = pygame.key.get_pressed()
    window.fill((0, 0, 0))

    # Basic movements
    if keys[pygame.K_LEFT]:
        player_vel_x = -player_vel
    if keys[pygame.K_RIGHT]:
        player_vel_x = player_vel
    if keys[pygame.K_UP]:
        player_vel_y = -player_vel
    if keys[pygame.K_DOWN]:
        player_vel_y = player_vel

    check_borders(player)
    # Shoot
    if keys[pygame.K_z]:
        if current_time - last_shot >= BULLET_DELAY:
            add_bullet = Bullet(player.rect.centerx, player.rect.top, speed_x=0, speed_y=-20)
            active_bullets.add(add_bullet)
            shoot.play()
            last_shot = current_time

    # Focus mode
    if keys[pygame.K_LSHIFT]:
        player_vel = 2.5

    # print(keys[pygame.K_z])

    if pygame.sprite.spritecollide(boss, active_bullets, True):
        print("hit")
        BOSS[0]["health"] -= 1


    # Damage handler
    if pygame.sprite.spritecollide(player, active_boss_bullets, True, collided=hitbox_collision):
        if current_time - immunity_latest >= IMMUNITY_PERIOD:
            print("Dead")
            PLR["lives"] -= 1
            deathsound.play()

            immunity_latest = current_time

        # player.rect.x = SCREEN_WIDTH / 2
        # player.rect.y = SCREEN_HEIGHT

    if PLR["lives"] < 1:
        game_state = 2

      
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x and PLR["bombs"] > 0:
                bomb = Bomb(player.rect.centerx, player.rect.centery)
                active_bombs.add(bomb)
                bomb_s.play()

                PLR["bombs"] -= 1


    active_bullets.update()

    for bullet in active_bullets:
        if bullet.rect.bottom < 0 or bullet.rect.top > SCREEN_HEIGHT:
            bullet.kill()

    for bossbullet in active_boss_bullets:
        if bossbullet.rect.bottom < 0 or bossbullet.rect.top > SCREEN_HEIGHT:
            bossbullet.kill()


    if game_state == 1:
        lives = font.render(f"Lives: {PLR["lives"]}", True, (255, 255, 255))
        lives_rect = lives.get_rect()
        lives_rect.topleft = (0, 60)
        bhealth = font.render(f"Boss Health: {BOSS[0]["health"]}", True, color=(255, 255, 255))
        bhealth_rect = bhealth.get_rect()
        bhealth_rect.topleft = (0, 120)
        bombs_left = font.render(f"Bombs: {PLR["bombs"]}", True, (255, 255, 255))
        bombs_rect = bombs_left.get_rect()
        bombs_rect.topleft = (0, 180)
        stars = font.render(f"Stars: {PLR["stars"]}", True, (255, 255, 255))
        stars_rect = stars.get_rect()
        stars_rect.topleft = (0, 240)
        player.rect.x += player_vel_x
        player.rect.y += player_vel_y

        if current_time - boss_last_shot >= BOSS_SHOOT_DELAY:
            print("Starting new volley:", rotation)
            shoot_spiral_curved(boss, 6, 5, rotation)
            rotation = (rotation + 15) % 360
            print("Boss bullet group size: ", len(active_boss_bullets))
            boss_last_shot = current_time

        # Draw thing.
        window.blit(player.image, player.rect)
        pygame.draw.rect(window, (0, 255, 0), player.hitbox, 1)
        window.blit(boss.image, boss.rect )
        window.blit(level, level_rect)
        window.blit(bhealth, bhealth_rect)
        window.blit(bombs_left, bombs_rect)
        window.blit(stars, stars_rect)
        window.blit(lives, lives_rect)
    
    elif game_state == 2:
        pygame.display.set_caption("Game over!")
        window.blit(game_over, game_rect)

    active_boss_bullets.update()
    active_bullets.draw(window)
    active_bombs.draw(window)
    active_boss_bullets.draw(window)
    active_bombs.update()
    player.update()
    pygame.display.flip()

    clock.tick(120)