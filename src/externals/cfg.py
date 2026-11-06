import pygame
from src.externals.characterinit import *

pygame.mixer.init()
pygame.init()
# current_time = pygame.time.get_ticks()
active_bullets = pygame.sprite.Group()
active_boss_bullets = pygame.sprite.Group()
active_bombs = pygame.sprite.Group()
active_drops = pygame.sprite.Group()
active_fp_drops = pygame.sprite.Group()
active_lv_drops = pygame.sprite.Group()

version = 1.4

BOMB_DURATION = 4000

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

CEN = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

deathsound = pygame.mixer.Sound('src/touhou-death-sound-effect.mp3')
deathsound.set_volume(.4)

shoot = pygame.mixer.Sound('src/graze.mp3')
shoot.set_volume(.3)

bomb_s = pygame.mixer.Sound('src/touhou-spellcard-warning-sfx.mp3')
bomb_s.set_volume(.6)

phase_new = pygame.mixer.Sound('src/touhou-old-powerup-sfx.mp3')
phase_new.set_volume(.5)

bossdeath = pygame.mixer.Sound('src/touhou-boss-death-sfx.mp3')
bossdeath.set_volume(.5)

MUSIC_QUEUE = {
    "menu": "",
    "game": "src/Native Faith.mp3",
    "game_over": "",
    "victory": ""
}

colour = {
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0)
}

FPS = 120

# Fonts

font = pygame.font.Font('window/THBiolinum.otf', 50)

level = font.render("Level: Front gate", True, colour["white"])
game_over = font.render("Game Over.", True, colour["white"])
game_done = font.render("You win!", True, colour["white"])

level_rect = level.get_rect()
level_rect.topleft = (0, 0)
game_rect = game_over.get_rect()
game_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 200)

es = font.render(f"Final score: {PLR["score"]} pts", True, colour["white"])
es_rect = es.get_rect()
es_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 100)