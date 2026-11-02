import pygame
pygame.mixer.init()
# current_time = pygame.time.get_ticks()
active_bullets = pygame.sprite.Group()
active_boss_bullets = pygame.sprite.Group()
active_bombs = pygame.sprite.Group()

BOMB_DURATION = 4000

CEN = (640, 360)

deathsound = pygame.mixer.Sound('touhou-death-sound-effect.mp3')
deathsound.set_volume(.4)

shoot = pygame.mixer.Sound('graze.mp3')
shoot.set_volume(.6)

bomb_s = pygame.mixer.Sound('touhou-spellcard-warning-sfx.mp3')
bomb_s.set_volume(.6)