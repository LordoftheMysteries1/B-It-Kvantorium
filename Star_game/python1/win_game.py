import pygame
import sys


add_x = 0
add_y = 0
new_level = False
l = 1
def win_level(screen):
    global add_x, new_level, l, add_y
    new_level = True
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Продолжить', 1, (180, 0, 0))
    button_rect = pygame.Rect(235, 300, 150, 50)
    button_surface = pygame.Surface((150, 50))
    text_rect = text1.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    text2 = f1.render('Выход', 1, (180, 0, 0))
    button_rect2 = pygame.Rect(235, 450, 150, 50)
    button_surface2 = pygame.Surface((150, 50))
    text_rect2 = text2.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect.collidepoint(event.pos):
                new_level = False
                return True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect2.collidepoint(event.pos):
                return 'menu'

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

    if button_rect2.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface2, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface2, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface2, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface2, (0, 100, 0), (1, 48, 148, 10), 2)


    button_surface.blit(text1, text_rect)
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    button_surface2.blit(text2, text_rect2)
    screen.blit(button_surface2, (button_rect2.x, button_rect2.y))


    pygame.display.update()


def l1():
    global add_x, add_y
    add_x = 200
    add_y = 0
def l2():
    global add_x, add_y
    add_x = 200
    add_y = 100
def l3():
    global add_x, add_y
    add_x = 300
    add_y = 100
def l4():
    global add_x, add_y
    add_x = 300
    add_y = 150

def count_enemy_x():
    global add_x
    return add_x
def count_enemy_y():
    global add_y
    return add_y

