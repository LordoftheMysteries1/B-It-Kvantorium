from itertools import count
from time import monotonic as timer
import pygame, volume, win_game, Pause
import sys
import time

from pygame.time import get_ticks

from bullet import Bullet
from enemy import Enemy
from boss import Boss
from enemy_bullet import enemy_Bullet

from win_game import new_level
import random

count = 0
damage = 0
lev = 1
money = 0
n_pause = False
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
start_time_boss = pygame.time.get_ticks()
double_shot_start_time = pygame.time.get_ticks()
# pygame.time.set_timer(pygame.USEREVENT, 1000)
timers = 0
sliv = False
timer_diration = 1000
spawn_diration = 3000
double_shot_duration = 500
boss5 = False
again1 = False
bflag = False
double_shot_pause = 100

def events(screen, ship, bullets, enemy_bullets, boss3, enemys, bullet_width, speed_bullet, double_shot):
    global n_pause, timers, start_time, start_time_boss, double_shot_start_time, bflag
    sound2_bullet = pygame.mixer.Sound('sounds/bullet.mp3')
    loudness1 = volume.volume4()
    n_pause = False
    #dt = clock.tick(60)
    curret_time = pygame.time.get_ticks()
    if boss3:
        curret_time = pygame.time.get_ticks()
        enemy_list = boss3.sprites()
        boss4 = enemy_list[0]
        if curret_time - start_time >= timer_diration:
            new_bullet_enemy = enemy_Bullet(screen, boss4)
            enemy_bullets.add(new_bullet_enemy)
            start_time = curret_time
        if curret_time - start_time_boss >= spawn_diration:
            spawn_bossarmy(screen, enemys)
            start_time_boss = curret_time
    if double_shot:
        if bflag:
            if curret_time - double_shot_start_time >= double_shot_duration:
                new_bullet = Bullet(screen, ship, bullet_width, speed_bullet, double_shot_pause)
                bullets.add(new_bullet)
                double_shot_start_time = curret_time
                bflag = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_RIGHT:
                ship.mright = True
            #влево
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
            #атака
            elif event.key == pygame.K_SPACE:

                new_bullet = Bullet(screen,ship, bullet_width, speed_bullet, 0)
                bullets.add(new_bullet)
                # for i in range(1, double_shot+1):

                sound2_bullet.play()
                sound2_bullet.set_volume(loudness1)
                if double_shot:
                    bflag = True

            elif event.key == pygame.K_ESCAPE:
                n_pause = True

        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            #влево
            elif event.key == pygame.K_LEFT:
                ship.mleft = False


def update_bullet(bullets, enemys, screen):
    global count
    loudness1 = volume.volume4()
    sound1_explosion_enemy = pygame.mixer.Sound('sounds/explosion enemy.mp3')
    # sound1_explosion_enemy.get_volume(loudness1)
    bullets.update()
    #спавн пули
    for bullet in bullets.sprites():
        bullet.rendering()
        bullet.update_pos()
        # sound2_bullet.play()
    #удаление пули
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            #
    # if pygame.sprite.spritecollideany(bullets, enemys):
    #     count += 1
    if pygame.sprite.groupcollide(bullets, enemys, True, True):
        sound1_explosion_enemy.play()
        sound1_explosion_enemy.set_volume(loudness1)
        count += 1
        #counting(screen)

    # не помню зачем это, оно сейчас не используется
    # collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)
    # print(collisions)
def level_defence(enemys):
    if enemys:
        adsd = 1
    else:
        return True

def k_pause():
    global n_pause, lev
    ex1 = Pause.exit()
    if n_pause:
        
        if ex1 == True:
            lev = 0
    return n_pause


def update_enemys(screen, ship, enemys):
    screen_rect = screen.get_rect()
    for enemy in enemys:
        enemy.update_pos()
        if boss5:
            continue
        else:
            if enemy.rect.bottom >= screen_rect.bottom:
                return True
                sys.exit()

    if pygame.sprite.spritecollideany(ship, enemys):
        return True
        sys.exit()




    #screen.fill(bg_color)

def update(bg_color, screen, ship, enemys, bullets, boss3):
    update_bullet(bullets, enemys, screen)
    update_enemys(screen, ship, enemys)
    counting(screen)
    leveling(screen)

    ship.rendering()
    enemys.draw(screen)
    pygame.display.flip()






def spawn_army(screen, enemys):
    global lev, boss5, again1
    boss5 = False
    if again1:
        add_level_enemy_x = 0
        add_level_enemy_y = 0
        again1 = False
    else:
        add_level_enemy_x = win_game.count_enemy_x()
        add_level_enemy_y = win_game.count_enemy_y()
    screen_w = screen.get_rect().width
    screen_h = screen.get_rect().height
    enemy = Enemy(screen)
    enemy_w = enemy.rect.width
    space_btwn = 25
    num_enemy_x = int((screen_w - 250 + add_level_enemy_x - 2 * enemy_w) / (enemy_w + space_btwn))
    # num_enemy_x = 4
    indent_x = int(((screen_w - num_enemy_x * (enemy_w + space_btwn)) + space_btwn) / 2)
    enemy_h = enemy.rect.height
    num_enemy_y = int((screen_h - 600 + add_level_enemy_y - 2 * enemy_h) / (enemy_h + space_btwn))
    # num_enemy_y = 1
    indent_y = int(((screen_h - 200 - num_enemy_y * (enemy_h + space_btwn)) + space_btwn) / 3)

    for i_row in range(num_enemy_y - 1):
        for i_enemy in range(num_enemy_x):
            enemy = Enemy(screen)
            enemy.x = indent_x + (enemy_w + space_btwn) * i_enemy
            enemy.y = indent_y + (enemy_h + space_btwn) * i_row
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            enemys.add(enemy)


def counting(screen):
    global count
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(f'Счет {count}', 1, (255, 255, 255))
    button_rect = pygame.Rect(0, 0, 150, 50)
    button_surface = pygame.Surface((150, 50))
    text_rect = text1.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))

    button_surface.set_colorkey((0, 0, 0))
    button_surface.blit(text1, text_rect)
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    return count

def loss(counted):
    global count
    count = counted

def shop():
    return money
def buy(something):
    global money
    if something == 'width':
        money -= 30
    if something == 'speed':
        money -= 20
    if something == 'double_shot':
        money -= 50
def leveling(screen):
    global count, lev

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(f'уровень {lev}', True, (255, 255, 255), None)
    button_rect = pygame.Rect(450, 0, 150, 50)
    button_surface = pygame.Surface((150, 50))
    image = pygame.Surface(
        (max(600, text1.get_width() + 10), text1.get_height() + 10),
        pygame.SRCALPHA
    )
    text_rect = text1.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))

    button_surface.set_colorkey((0, 0, 0))
    button_surface.blit(text1, text_rect)
    screen.blit(button_surface, (button_rect.x, button_rect.y))

def again():
    global count, lev, again1, money
    lev = 1
    money += count
    count = 0
    again1 = True


def count_lev():
    global lev
    lev += 1



def update_bullet_boss(bullets, boss3, enemys):
    global count, damage
    loudness1 = volume.volume4()
    sound1_explosion_enemy = pygame.mixer.Sound('sounds/explosion enemy.mp3')
    bullets.update()
    #спавн пули
    for bullet in bullets.sprites():
        bullet.rendering()
        bullet.update_pos()
        # sound2_bullet.play()
    #удаление пули
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # if pygame.sprite.spritecollideany(bullets, enemys):
    if pygame.sprite.groupcollide(bullets, boss3, True, False):
        sound1_explosion_enemy.play()
        sound1_explosion_enemy.set_volume(loudness1)
        count += 1
        damage += 1
    if pygame.sprite.groupcollide(bullets, enemys, True, True):
        sound1_explosion_enemy.play()
        sound1_explosion_enemy.set_volume(loudness1)
        count += 1


def update_enemy_bullet(enemy_bullets, ship):
    global count, sliv
    enemy_bullets.update()
    #спавн пули
    for bullet in enemy_bullets.sprites():
        bullet.rendering()
        bullet.update_pos()
        # sound2_bullet.play()
    #удаление пули
    for bullet in enemy_bullets.copy():
        if bullet.rect.bottom >= 850:
            enemy_bullets.remove(bullet)
            #
    # if pygame.sprite.spritecollideany(bullets, enemys):
    #     count += 1
    if pygame.sprite.spritecollideany(ship, enemy_bullets):
         sliv = True

def checkig():
    global sliv
    return sliv


def update_boss(screen, boss3, bullets):
    global damage
    screen_rect = screen.get_rect()
    for i in boss3:
        i.update_pos()
    if damage == 100:
        pygame.sprite.groupcollide(bullets, boss3, True, True)

def update_bosses(screen, bg_color, boss3, bullets, enemys, ship, enemy_bullets):
    boss3.draw(screen)
    enemys.draw(screen)
    update_boss(screen, boss3, bullets)
    ship.rendering()
    update_bullet_boss(bullets, boss3, enemys)
    # event_enemy_bullet(screen, ship, enemy_bullets)
    update_enemy_bullet(enemy_bullets, ship)
    update_enemys(screen, ship, enemys)


def spawn_boss(screen, boss3):
    global sliv, boss5
    boss5 = True
    sliv = False
    boss2 = Boss(screen)
    boss2.rect.x = 300
    boss2.rect.y = 200
    boss3.add(boss2)

def spawn_bossarmy(screen, enemys):
    screen_w = screen.get_rect().width
    screen_h = screen.get_rect().height
    enemy = Enemy(screen)
    enemy_w = enemy.rect.width
    space_btwn = random.randint(25, 200)
    #num_enemy_x = int((screen_w - 2 * enemy_w) / (enemy_w + space_btwn))
    num_enemy_x = 3
    #indent_x = int(((screen_w - num_enemy_x * (enemy_w + space_btwn)) + space_btwn) / 2)
    indent_x = random.randint(30, 175)
    enemy_h = enemy.rect.height
    #num_enemy_y = int((screen_h - 2 * enemy_h) / (enemy_h + space_btwn))
    num_enemy_y = 2
    indent_y = int(((screen_h - 200 - num_enemy_y * (enemy_h + space_btwn)) + space_btwn) / 3)

    for i_row in range(num_enemy_y - 1):
        for i_enemy in range(num_enemy_x):
            enemy = Enemy(screen)
            enemy.x = indent_x + (enemy_w + space_btwn) * i_enemy
            enemy.y = indent_y + (enemy_h + space_btwn) * i_row
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            enemys.add(enemy)















