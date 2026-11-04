import pygame
from src.externals.classes import *
from src.externals.characterinit import *
from src.externals.cfg import *
import math
import json

# def settings_load():
#     with open('src/settings.json', 'r') as f:
#         data = json.load(f)

#     return data

# def apply_settings():
#     with open('src/settings.json', 'w') as f:

def check_borders(player):
    if player.rect.y >= 630:
        player.rect.y = 630
    if player.rect.x >= 1200:
        player.rect.x = 1200
    if player.rect.y <= 0:
        player.rect.y = 0
    if player.rect.x <= 0:
        player.rect.x = 0
    
def get_current_time():
    return pygame.time.get_ticks()

def shoot_spread(boss, bullet_amt, spread_angle, speed):
    print("called shoot_spread.")
    for i in range(bullet_amt):

        angle = math.radians(
            90 - spread_angle / 2
            + i * spread_angle / (bullet_amt - 1)
        )

        bullet_vx = speed * math.cos(angle)
        bullet_vy = speed * math.sin(angle)

        bullet = BossBullet(
            boss.rect.centerx, 
            boss.rect.centery,
            bullet_vx,
            bullet_vy
        )
        active_boss_bullets.add(bullet)

def shoot_radial(boss, bullet_amt, speed):
    for i in range(bullet_amt):
        angles = math.radians((360 / bullet_amt) * i)

        bullet_vx = speed * math.cos(angles)
        bullet_vy = speed * math.sin(angles)

        bullet = BossBullet(
                        boss.rect.centerx, 
                        boss.rect.centery,
                        bullet_vx,
                        bullet_vy
                    )
    # print("created bullet at: {} ({}, {})".format(bullet.rect.center, bullet_vx, bullet_vy))
        active_boss_bullets.add(bullet)

def shoot_spiral(boss, bullet_amt, speed, rotation):
    for i in range(bullet_amt):
        angle = math.radians((360 / bullet_amt) * i + rotation)
        bullet_vx = speed * math.cos(angle)
        bullet_vy = speed * math.sin(angle)

        bullet = BossBullet(
            boss.rect.centerx,
            boss.rect.centery,
            bullet_vx,
            bullet_vy
        )

        print(f"Rotation: {rotation} | VX: {bullet_vx:.2f} | VY: {bullet_vy:.2f}")
        active_boss_bullets.add(bullet)

def shoot_spiral_curved(boss, bullet_amt, speed, rotation):
    for i in range(bullet_amt):
        angle = math.radians((360 / bullet_amt) * i + rotation)
        bullet_vx = speed * math.cos(angle)
        bullet_vy = speed * math.sin(angle)
        

        bullet = BossBulletCurve(
            boss.rect.centerx,
            boss.rect.centery,
            bullet_vx,
            bullet_vy,
            turn_speed=.5
        )

        print(f"Rotation: {rotation} | VX: {bullet_vx:.2f} | VY: {bullet_vy:.2f}")
        active_boss_bullets.add(bullet)

def hitbox_collision(player, bullet):
    return player.hitbox.colliderect(bullet.rect)

def boss_logic(boss, BOSS_SHOOT_DELAY, current_time, phase, rotation, boss_last_shot):
    if current_time - boss_last_shot >= BOSS_SHOOT_DELAY:
        # print("Starting new volley:", rotation)
        if phase < len(BOSS): 
            boss_ptn = BOSS[phase]["pattern"]
            print("Current pattern:", boss_ptn)
            if boss_ptn == 1: # Spread
                shoot_spread(boss, 24, 360, 7)
                # print("Shooting spread")
            elif boss_ptn == 2: # Spiral
                shoot_spiral(boss, 18, 5, rotation)
                # print("Shooting spiral")
            elif boss_ptn == 3: # Radial
                shoot_radial(boss, 6, 3)
                # print("Shooting radial")
            elif boss_ptn == 4: # Spiral curved
                shoot_spiral_curved(boss, 7, 5, rotation)
                rotation = (rotation + 15) % 360
                # print("Shooting spiral (curved)")
            else:
                return "illegal!"
        
        # print("Boss bullet group size: ", len(active_boss_bullets))
        boss_last_shot = current_time

    return rotation, boss_last_shot

def remove_offscreen_bullets(active_bullets, active_boss_bullets):
    screen_rect = pygame.display.get_surface().get_rect()

    for group in (active_bullets, active_boss_bullets):
        for bullet in group:
            if not screen_rect.colliderect(bullet.rect):
                bullet.kill()


def music_handler(state):
    desired_music = None
    if state == 0: # Main menu
        desired_music = MUSIC_QUEUE["menu"]
    elif state == 1: # Main game
        desired_music = MUSIC_QUEUE["game"]
    elif state == 2:
        desired_music = MUSIC_QUEUE["game_over"]
    elif state == 3:
        desired_music = MUSIC_QUEUE["victory"]
    return desired_music