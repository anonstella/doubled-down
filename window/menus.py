import pygame
from src.externals.cfg import *
from src.externals.save_mechanics import *

pygame.init()


font_title = pygame.font.Font('window/THBiolinum.otf', 80)

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
quit_rect.topleft = (80, 350)

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

def settings(window):
    pygame.display.set_caption("東方: Doubled Down - settings")
    window.blit(title_settings, title_settings_rect)
    save = load_save()



def draw_selmain(opt):
    if opt == 1:
        # sel_rect.topleft = (220, 350)
        sel_rect.topleft = (170, 350)
    # elif opt == 2:
    #     sel_rect.topleft = (170, 450)

    else:
        sel_rect.topleft = (170, 250)
        
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