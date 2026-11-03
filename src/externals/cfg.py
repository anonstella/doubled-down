import pygame
pygame.mixer.init()
# current_time = pygame.time.get_ticks()
active_bullets = pygame.sprite.Group()
active_boss_bullets = pygame.sprite.Group()
active_bombs = pygame.sprite.Group()

BOMB_DURATION = 4000

CEN = (640, 360)

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