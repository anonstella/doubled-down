import pygame
from src.externals.classes import *
from src.externals.characterinit import *
from src.externals.functions import *
from src.externals.cfg import *
from window.menus import *

# Game idea: Doubled Down
# Concept: A game where you have to dodge incoming drone attacks. Use your dodging skills to evade the bullets!
# Inspiration: Touhou franchise / Bullet hell

pygame.init()

pygame.mixer.init()

save = load_save()


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("東方: Doubled Down - ver. {}".format(version))
clock = pygame.time.Clock()

menu_opt, over_opt, vic_opt = 0, 0, 0

game_state = 3

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

player = Player()


# Player's bullet
BASE_BULLET_DELAY, BOSS_SHOOT_DELAY, IMMUNITY_PERIOD = 14, 240, 1500 # milliseconds
BULLET_DELAY = BASE_BULLET_DELAY
last_shot, boss_last_shot, immunity_latest = 0, 0, 0

player_vel = 5

screen_rect = window.get_rect()
player.rect.clamp_ip(screen_rect)

rotation, phase, last_phase_change = 0, 0, 0
PHASE_PERIOD = 3000 # ms
transition_start = 0
phase_trans, summoned = False, False
healthbar = BossHealthBar(0, 30, 250, 30, BOSS[phase]["health"])

current_music = None

boss = Boss_Mod(BOSS[phase])
# boss = Boss()

def reset_game(): # resets stuff
    global phase, rotation, phase_trans
    global boss_last_shot, last_shot, immunity_latest

    PLR["lives"] = 5
    PLR["bombs"] = 3
    PLR["stars"] = 0
    PLR["score"] = 0

    phase = 0
    rotation = 0
    phase_trans = False

    boss_last_shot = get_current_time()
    last_shot = 0
    immunity_latest = 0

    for group in (active_bullets, active_boss_bullets, active_bombs):
        group.empty()

    for i, boss_data in enumerate(BOSS):
        boss_data["health"] = [1000, 1450, 2000, 2300, 2540, 3000][i] # This is kinda bad coding practice, cuz if more phases are added, then this is kinda impractical.

while True:
    # print(PLR["score"])
    current_time = get_current_time()
    # fix players vel to 0 every frame with no keyboard input.
    player_vel_x = 0
    player_vel_y = 0

    player_vel = 5


    # firepower update (ver. 1.4)
    BULLET_DELAY = update_firepower(BASE_BULLET_DELAY)
    # print(BULLET_DELAY)
    # print(PLR["score"], PLR["firepower_addition"], BULLET_DELAY)

    # Border check
    keys = pygame.key.get_pressed()
    window.fill((0, 0, 0))

    if game_state == 1: # game
    # Focus mode
        if keys[pygame.K_LSHIFT]:
            player_vel = 2.5

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
                straight, left, right, leftm, rightm = bullet_formation(player)
                active_bullets.add(straight, left, right, leftm, rightm)
                shoot.play()
                last_shot = current_time

    if not phase_trans:
        if pygame.sprite.spritecollide(boss, active_bullets, True):
            if phase < len(BOSS):
                BOSS[phase]["health"] -= 1


    # Damage handler
    if pygame.sprite.spritecollide(player, active_boss_bullets, True, collided=hitbox_collision):
        if current_time - immunity_latest >= IMMUNITY_PERIOD:
            phase_trans
            print("Dead")
            PLR["lives"] -= 1
            deathsound.play()

            immunity_latest = current_time

    # points handler
    if pygame.sprite.spritecollide(player, active_drops, True, collided=drop_collision):
        PLR["score"] += 12500

    # fp handler
    if pygame.sprite.spritecollide(player, active_fp_drops, True, collided=drop_collision):
        PLR["firepower_addition"] += 1
   
    # lv handler
    if pygame.sprite.spritecollide(player, active_fp_drops, True, collided=drop_collision):
        PLR["lives"] += 1

    if phase < len(BOSS) and game_state == 1:
        if BOSS[phase]["health"] < 1 and not phase_trans:
            phase_trans = True
            transition_start = current_time
            # deathsound.play()
            bossdeath.play()
        if PLR["lives"] < 1:
            game_state = 2

    # if phase >= len(BOSS) - 1:
    #     game_state = 3
    if player.rect.y <= 250: # Player on collect zone
        for item in active_drops:
            item.home_to_player(player)
        for item in active_fp_drops:
            item.home_to_player(player)
        for item in active_lv_drops:
            item.home_to_player(player)
    
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x and PLR["bombs"] > 0 and game_state == 1:
                bomb = Bomb(player.rect.centerx, player.rect.centery)
                active_bombs.add(bomb)
                bomb_s.play()

                PLR["bombs"] -= 1

            if game_state == 0: # menu
                if event.key == pygame.K_DOWN:
                    if menu_opt == 2:
                        menu_opt = 0
                        select.play()
                    else:
                        menu_opt += 1
                        select.play()

                if event.key == pygame.K_UP:
                    if menu_opt == 0:
                        menu_opt = 2
                        select.play()
                    else:
                        menu_opt -= 1
                        select.play()

                if event.key == pygame.K_z:
                    if menu_opt == 2:
                        click.play()
                        pygame.quit()
                        sys.exit(0)
                    elif menu_opt == 1:
                        game_state = 4
                        click.play()
                    else:
                        game_state = 1
                        click.play()

            if game_state == 2:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    if over_opt == 1:
                        over_opt = 0
                        select.play()
                    else:
                        over_opt = 1
                        select.play()

                if event.key == pygame.K_z:
                    if over_opt == 1:
                        game_state = 0
                        click.play()
                    else:
                        reset_game()
                        game_state = 1
                        click.play()

            if game_state == 3:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    if vic_opt == 1:
                        vic_opt = 0
                        select.play()
                    else:
                        vic_opt = 1
                        select.play()

                if event.key == pygame.K_z:
                    if vic_opt == 0:
                        reset_game()
                        game_state = 1
                        click.play()
                    else:
                        game_state = 0
                        click.play()

            if game_state == 5:
                if event.key == pygame.K_DOWN:
                    if settings_opt == 2:
                        settings_opt = 0
                        select.play()
                    else:
                        settings_opt += 1
                        select.play()

                if event.key == pygame.K_UP:
                    if settings_opt == 0:
                        settings_opt =2
                        select.play()
                    else:
                        settings_opt -= 1
                        select.play()

                if event.key == pygame.K_LEFT: # reduce by .1 (equivalent to 10 when multiplied by 100)
                    if settings_opt == 0 and temp_opt1 >= 0:
                        temp_opt1 -= 10
                        temp_opt1 = max(0, temp_opt1)
                        print("music vol - 10: ", temp_opt1)
                        music_v_test.set_volume(temp_opt1 / 100)
                        music_v_test.play()
                    if settings_opt == 1 and temp_opt2 >= 0:
                        temp_opt2 -= 10
                        temp_opt2 = max(0, temp_opt2)
                        print("sfx vol - 10: ", temp_opt2)
                        shoot.set_volume(temp_opt2 / 100)
                        shoot.play()
                if event.key == pygame.K_RIGHT:
                    if settings_opt == 0 and temp_opt1 <= 100:
                        temp_opt1 += 10
                        temp_opt1 = max(0, min(100, temp_opt1))
                        print("music vol + 10: ", temp_opt1)
                        music_v_test.set_volume(temp_opt1 / 100)
                        music_v_test.play()
                    if settings_opt == 1 and temp_opt2 <= 100:
                        temp_opt2 += 10
                        temp_opt2 = max(0, min(100, temp_opt2))
                        print("sfx vol + 10: ", temp_opt2)
                        shoot.set_volume(temp_opt2 / 100)
                        shoot.play()

                if event.key == pygame.K_z:
                    if settings_opt == 2:
                        game_state = 0
                        click.play()
                    else:
                        save["music_vol"] = temp_opt1
                        save["sfx_vol"] = temp_opt2
                        w_save(save)
                        print('Saved!')
                        click.play()

    active_bullets.update()

    desired_music = music_handler(game_state)

    if desired_music != current_music:
        if not desired_music == "" and not desired_music == None:
            pygame.mixer.music.load(resource_path(desired_music))
            pygame.mixer.music.set_volume(music_v)
            pygame.mixer.music.play(-1)
            current_music = desired_music
        else:
            pygame.mixer.music.fadeout(3000)
            current_music = None
    
    for bullet in active_bullets:
        if bullet.rect.bottom < 0 or bullet.rect.top > SCREEN_HEIGHT:
            bullet.kill()

    for bossbullet in active_boss_bullets:
        if bossbullet.rect.bottom < 0 or bossbullet.rect.top > SCREEN_HEIGHT:
            bossbullet.kill()

    
    if phase_trans:
        if not summoned:
            summon_drops(phase)
            summoned = True
        else:
            pass
        if current_time - transition_start >= PHASE_PERIOD:
            phase += 1
            if phase < len(BOSS):
                # BOSS[phase]["health"] = 0
                # phase += 1
                boss = Boss_Mod(BOSS[phase])
                phase_trans = False
                boss_last_shot = current_time
                summoned = False
            else:
                game_state = 3

    if game_state == 0: # Main menu
        pygame.display.set_caption("東方: Doubled Down - ver. {}".format(version))
        main_menu(window)
        draw_selmain(menu_opt)
    if game_state == 1:
        pygame.display.set_caption("東方: Doubled Down - Game phase")
        lives = font.render(f"Lives: {PLR["lives"]}", True, (255, 255, 255))
        lives_rect = lives.get_rect()
        lives_rect.topleft = (0, 60)
        # bhealth = font.render(f"Boss Health: {BOSS[phase]["health"] if phase < len(BOSS) else ""}", True, color=(255, 255, 255))
        # bhealth_rect = bhealth.get_rect()
        # bhealth_rect.topleft = (0, 120)
        bombs_left = font.render(f"Bombs: {PLR["bombs"]}", True, (255, 255, 255))
        bombs_rect = bombs_left.get_rect()
        bombs_rect.topleft = (0, 120)
        score = font.render(f"Score: {PLR["score"]}", True, colour["white"])
        scores_rect = score.get_rect()
        scores_rect.topleft = (0, 180)
        # scores_rect.topleft = (0, 240)
        player.rect.x += player_vel_x
        player.rect.y += player_vel_y

        if not phase_trans:
            rotation, boss_last_shot = boss_logic(boss, BOSS_SHOOT_DELAY, current_time, phase, rotation, boss_last_shot)
            window.blit(boss.image, boss.rect)

        # Update the boss's health
        healthbar.current = BOSS[phase]["health"]

        # Draw thing.  
        window.blit(player.image, player.rect)
        healthbar.draw(window)
        pygame.draw.rect(window, (0, 255, 0), player.hitbox, 1)
        # window.blit(level, level_rect)
        window.blit(score, scores_rect)
        # window.blit(bhealth, bhealth_rect)
        window.blit(bombs_left, bombs_rect)
        # window.blit(stars, stars_rect)
        window.blit(lives, lives_rect)
    
    elif game_state == 2:
        es = font.render(f"Final score: {PLR["score"]} pts", True, colour["white"])
        es_rect = es.get_rect()
        es_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 100)
        window.blit(es, es_rect)
        gameover(window)
        draw_selover(over_opt)
        
    
    elif game_state == 3:
        es = font.render(f"Final score: {PLR["score"]} pts", True, colour["white"])
        es_rect = es.get_rect()
        es_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 100)
        window.blit(es, es_rect)
        victory(window)
        draw_selwon(vic_opt)

    elif game_state == 4:
        # save = load_save()
        temp_opt1 = save["music_vol"]
        temp_opt2 = save["sfx_vol"]
        game_state = 5
    elif game_state == 5: # settings page
        settings(window, temp_opt1, temp_opt2, save)
        draw_selset(settings_opt)
        
        

    active_boss_bullets.update()
    remove_offscreen_bullets(active_bullets, active_boss_bullets, active_drops, active_fp_drops, active_lv_drops)
    active_bullets.draw(window)
    active_bombs.draw(window)
    active_drops.draw(window)
    active_drops.update()
    active_fp_drops.draw(window)
    active_fp_drops.update()
    active_lv_drops.draw(window)
    active_lv_drops.update()
    active_boss_bullets.draw(window)
    active_bombs.update()
    player.update()
    pygame.display.flip()

    clock.tick(FPS)