import pygame
from src.externals.characterinit import *
from src.externals.initializer import *
from src.externals.save_mechanics import *

pygame.mixer.init()
pygame.init()
# current_time = pygame.time.get_ticks()
active_bullets = pygame.sprite.Group()
active_boss_bullets = pygame.sprite.Group()
active_bombs = pygame.sprite.Group()
active_drops = pygame.sprite.Group()
active_fp_drops = pygame.sprite.Group()
active_lv_drops = pygame.sprite.Group()

version = 1.5

BOMB_DURATION = 4000

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

CEN = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

save = load_save()

music_v = save['music_vol'] / 100
sfx_v = save['sfx_vol'] / 100
deathsound = pygame.mixer.Sound(resource_path('src/touhou-death-sound-effect.mp3'))
deathsound.set_volume(sfx_v)

shoot = pygame.mixer.Sound(resource_path('src/graze.mp3'))
shoot.set_volume(sfx_v)

bomb_s = pygame.mixer.Sound(resource_path('src/touhou-spellcard-warning-sfx.mp3'))
bomb_s.set_volume(sfx_v)

select = pygame.mixer.Sound(resource_path('src/leappad3-click-sound.mp3'))
select.set_volume(sfx_v)

music_v_test = pygame.mixer.Sound(resource_path('src/scribblenauts-button-click.mp3'))
music_v_test.set_volume(music_v)

click = pygame.mixer.Sound(resource_path('src/test-select-2.mp3'))
click.set_volume(sfx_v)

phase_new = pygame.mixer.Sound(resource_path('src/touhou-old-powerup-sfx.mp3'))
phase_new.set_volume(sfx_v)

bossdeath = pygame.mixer.Sound(resource_path('src/touhou-boss-death-sfx.mp3'))
bossdeath.set_volume(sfx_v)


MUSIC_QUEUE = {
    "menu": "src/AdhesiveWombat - Night Shade.mp3",
    "game": "src/Native Faith.mp3",
    "game_over": "",
    "victory": ""
}

colour = {
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "yellow": (255, 255, 0)
}

FPS = 120

# settings
settings_opt = 0
temp_opt1 = 0
temp_opt2 = 0

# Fonts

font = pygame.font.Font(resource_path('src/THBiolinum.otf'), 50)

# level = font.render("Level: Front gate", True, colour["white"])
game_over = font.render("Game Over.", True, colour["white"])
game_done = font.render("You win!", True, colour["white"])

# level_rect = level.get_rect()
# level_rect.topleft = (0, 0)
game_rect = game_over.get_rect()
game_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 200)

es = font.render(f"Final score: {PLR["score"]} pts", True, colour["white"])
es_rect = es.get_rect()
es_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 100)