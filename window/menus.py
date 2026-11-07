import pygame
from src.externals.cfg import *
from src.externals.save_mechanics import *
from src.externals.initializer import *

pygame.init()


font_title = pygame.font.Font(resource_path('src/THBiolinum.otf'), 80)

title = font_title.render('Touhou: Doubled Down', True, colour["white"])
title_settings = font_title.render('Settings', True, colour["white"])

play = font.render('Play', True, colour["white"])
# options = font.render('Options', True, colour["white"])
quit_opt = font.render('Quit', True, colour["white"])

title_rect = title.get_rect()
title_rect.topleft = (30, 20)

title_settings_rect = title.get_rect()
title_settings_rect.topleft = (30, 20)

play_rect = play.get_rect()
play_rect.topleft = (80, 250)
# options_rect = options.get_rect()
# options_rect.topleft = (80, 350)
quit_rect = quit_opt.get_rect()
quit_rect.topleft = (80, 450)
settings_ = font.render('Settings', True, colour["white"])

settings_rect = settings_.get_rect()
settings_rect.topleft = (80, 350)

retry = font.render('Try again', True, colour["white"])
again = font.render('Play again', True, colour["white"])
menu = font.render('Main Menu', True, colour["white"])

retry_rect = retry.get_rect()
retry_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

again_rect = again.get_rect()
again_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

menu_rect = menu.get_rect()
menu_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)


sel = font.render('<', True, colour["white"])

sel_rect = sel.get_rect()

def main_menu(window):
    window.blit(title, title_rect)
    window.blit(play, play_rect)
    window.blit(settings_, settings_rect)
    window.blit(quit_opt, quit_rect)
    window.blit(sel, sel_rect)

def gameover(window):
    pygame.display.set_caption("東方: Doubled Down - Game over!")
    window.blit(game_over, game_rect)
    window.blit(retry, retry_rect)
    window.blit(menu, menu_rect)
    window.blit(sel, sel_rect)

def victory(window):
    pygame.display.set_caption("東方: Doubled Down - You win!")
    window.blit(again, again_rect)
    window.blit(game_done, game_rect)
    window.blit(menu, menu_rect)
    window.blit(sel, sel_rect)

back = font.render(f'Back', True, colour["white"])
def settings(window, t1, t2, save):
    pygame.display.set_caption("東方: Doubled Down - settings")
    music_v = font.render(f'Music volume: {t1}', True, colour["white"])
    sfx_v = font.render(f'SFX volume: {t2}', True, colour["white"])
    
    music_v_rect = music_v.get_rect()
    sfx_v_rect = sfx_v.get_rect()
    music_v_rect.topleft = (30, 200)
    sfx_v_rect.topleft = (30, 300)
    back_rect = back.get_rect()
    back_rect.topleft = (30, 400)

    if t1 != save['music_vol']:
        music_v = font.render(f'Music volume: {t1}', True, colour["yellow"])
    if t2 != save['sfx_vol']:
        sfx_v = font.render(f'SFX volume: {t2}', True, colour["yellow"])

    window.blit(title_settings, title_settings_rect)
    window.blit(music_v, music_v_rect)
    window.blit(sfx_v, sfx_v_rect)
    window.blit(back, back_rect)
    window.blit(sel, sel_rect)



def draw_selmain(opt):
    if opt == 1:
        # sel_rect.topleft = (220, 350)
        sel_rect.topleft = (220, 350)
    elif opt == 2:
        sel_rect.topleft = (220, 450)

    else:
        sel_rect.topleft = (220, 250)
        
def draw_selover(opt):
    if opt == 0:
        sel_rect.center = ((SCREEN_WIDTH / 2) + 150, (SCREEN_HEIGHT / 2))
    else:
        sel_rect.center = ((SCREEN_WIDTH / 2) + 150, (SCREEN_HEIGHT / 2) + 100)

def draw_selwon(opt):
    if opt == 0:
        sel_rect.center = ((SCREEN_WIDTH / 2) + 150, (SCREEN_HEIGHT / 2))
    else:
        sel_rect.center = ((SCREEN_WIDTH / 2) + 150, (SCREEN_HEIGHT / 2) + 100)

def draw_selset(opt):
    if opt == 0:
        sel_rect.topleft = (400, 200)
    elif opt == 1:
        sel_rect.topleft = (400, 300)
    else:
        sel_rect.topleft = (400, 400)