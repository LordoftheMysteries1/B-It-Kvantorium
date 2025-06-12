from pprint import pformat
from turtledemo.penrose import start

import pygame, controls, menu, settings, screen_det, volume, win_game, end_game, Pause, shop
from boss import Boss
# from menu import start_game
import sys, time
from bullet import Bullet

from pygame.examples.music_drop_fade import music_can_seek

from ship import Ship
from pygame.sprite import Group
#from enemy import Enemy
# from menu import menu

loudness = 0.6
lflag = 1
level = 0
bullet_width = 20
speed_bullet = 0
double_shot = False
F = True
fboss = False
fmusic = True
fagain = False
l = [0, 3, 8, 18, 30, 48]




def run():
    global loudness, lflag, level, F, fboss

    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    background = pygame.image.load("images/background.jpg")  # !!! установите свое .jpg
    rect = background.get_rect()
    background = pygame.transform.scale(background, (600, 900))
    bg_color = (0, 0, 0)
    spaceship = Ship(screen)
    bullets = Group()
    enemy_bullets = Group()
    boss3 = Group()
    #enemy = Enemy(screen)
    enemys = Group() 
    if fboss:
        controls.spawn_boss(screen, boss3)
    else:
        controls.spawn_army(screen, enemys)
    
    # sstart_game = False

    count = 0

    while 42:

        controls.events(screen, spaceship, bullets, enemy_bullets,boss3, enemys, bullet_width, speed_bullet, double_shot)
        spaceship.update_pos()
        if fboss:
            controls.update_bosses(screen, bg_color, boss3, bullets, enemys, spaceship, enemy_bullets)
        else:
            controls.update(bg_color, screen, spaceship, enemys, bullets, boss3)
        #controls.leveling(screen)
        count = controls.counting(screen)
        defence = controls.level_defence(enemys)
        q_pause = controls.k_pause()

        if controls.checkig():
            controls.loss(l[lflag - 1])
            detching()

        pygame.display.update()

        if q_pause:
            controls.loss(l[lflag - 1])
            pause()

        if fboss:
            b = 2
        else:
            if lflag == 5 and defence == True:
                fboss = True
                lflag += 1
                level += 1
                controls.count_lev()
                win()
            if defence:
                lflag += 1
                level += 1
                controls.count_lev()
                win()

        match count, lflag:
            case (3, 1) | (8, 2) | (18, 3) | (30, 4):
                lflag += 1
                level += 1
                controls.count_lev()
                win()
            case 48, 5:
                fboss = True
                lflag += 1
                level += 1
                controls.count_lev()
                win()
            case 75, 6:
                end_game1()

        deid = controls.update_enemys(screen, spaceship, enemys)
        if deid:
            controls.loss(l[lflag-1])
            detching()

        screen.blit(background, (0, 0))




def main_menu():
    # pygame.mixer.music.set_volume(0)
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    music()
    while 42:
        start_game = menu.menu(screen)
        if start_game == True:
            run()
            sys.exit()
        if start_game == 'exit':
            sys.exit()
        if start_game == 'settings':
            sett()
            sys.exit()
        if start_game == 'shop':
            shop1()
            sys.exit()

def sett():
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    while 42:
        parametr = settings.settings(screen)
        if parametr == 'exit':
            main_menu()
            sys.exit()
        if parametr:
            volume1()


def detching():
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    while 42:
        returned = screen_det.detch(screen)
        if returned == True:
            run()
            sys.exit()

def volume1():
    global loudness
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    while 42:
        value = volume.volume3(screen)
        music()
        match value:
            case 1:
                loudness = 0.5
            case 2:
                loudness = 0.75
            case 3:
                loudness = 1
            case 4:
                sett()

def music():
    global fmusic
    pygame.init()
    if fmusic:
        pygame.mixer.music.load('sounds/music.mp3')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(loudness)
        fmusic = False
    else:
        pygame.mixer.music.set_volume(loudness)

def win():
    global level
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    match level:
        case 1:
            win_game.l1()
        case 2:
            win_game.l2()
        case 3:
            win_game.l3()
        case 4:
            win_game.l4()
    while 42:
        count = controls.counting(screen)
        winning = win_game.win_level(screen)
        if winning:
            run()
        if winning == 'menu':
            main_menu()


def end_game1():
    global level, lflag, fboss, fagain
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    while 42:
        ending = end_game.end_game1(screen)
        if ending == 'menu':
            controls.again()
            level = 0
            lflag = 1
            fboss = False
            fagain = True
            main_menu()



def pause():
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    while 42:
        w_pause = Pause.pause1(screen)
        if w_pause == True:
            run()
        if w_pause == 'exit':
            main_menu()

def shop1():
    global bullet_width, speed_bullet, double_shot
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Защитник космичского пространства")
    while 42:
        money_shop = controls.shop()
        shoping = shop.shop2(screen, money_shop)
        if shoping == 'exit':
            main_menu()
        if shoping == 'speed':
            controls.buy('speed')
            speed_bullet += 0.5
        if shoping == 'width':
            controls.buy('width')
            bullet_width += 10
        if shoping == 'double_shot':
            controls.buy('double_shot')
            double_shot = True



main_menu()


