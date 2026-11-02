import pygame
from src.externals.classes import *
from src.externals.cfg import *
import math

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