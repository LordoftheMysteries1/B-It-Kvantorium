from turtledemo.penrose import start

import pygame
import sys


from pygame.examples.scrap_clipboard import screen


# from game import start_game
# class menu:()
#     def __init__(self, screen):

# start_game = False

def shop2(screen, money_shop):
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('увелчить скорость 20', 1, (180, 0, 0))
    button_rect = pygame.Rect(185, 200, 300, 50)
    button_surface = pygame.Surface((300, 50))
    text_rect = text1.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    text2 = f1.render('увеличить ширину 30', 1, (180, 0, 0))
    button_rect2 = pygame.Rect(185, 350, 300, 50)
    button_surface2 = pygame.Surface((300, 50))
    text_rect2 = text2.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    text3 = f1.render('Выход', 1, (180, 0, 0))
    button_rect3 = pygame.Rect(250, 650, 150, 50)
    button_surface3 = pygame.Surface((150, 50))
    text_rect3 = text3.get_rect(
        center=(button_surface3.get_width() / 2,
                button_surface3.get_height() / 2))
    text4 = f1.render('Удвоить выстрел 50', 1, (180, 0, 0))
    button_rect4 = pygame.Rect(185, 500, 300, 50)
    button_surface4 = pygame.Surface((300, 50))
    text_rect4 = text4.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))

    text5 = f1.render(f'Деньги: {money_shop}', True, (255, 255, 255), None)
    button_rect5 = pygame.Rect(0, 0, 150, 50)
    button_surface5 = pygame.Surface((150, 50))
    text_rect5 = text5.get_rect(
        center=(button_surface5.get_width() / 2,
                button_surface5.get_height() / 2))

    text6 = f1.render(f'Недостаточно средств', True, (255, 255, 255), None)
    button_rect6 = pygame.Rect(185, 150, 300, 50)
    button_surface6 = pygame.Surface((300, 50))
    text_rect6 = text6.get_rect(
        center=(button_surface6.get_width() / 2,
                button_surface6.get_height() / 2))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect.collidepoint(event.pos):
                if money_shop >= 20:
                    return 'speed'
                else:
                    button_surface6.blit(text6, text_rect6)
                    screen.blit(button_surface6, (button_rect6.x, button_rect6.y))


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect3.collidepoint(event.pos):
                return 'exit'

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect2.collidepoint(event.pos):
                if money_shop >= 30:
                    return 'width'
                else:
                    button_surface6.blit(text6, text_rect6)
                    screen.blit(button_surface6, (button_rect6.x, button_rect6.y))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect4.collidepoint(event.pos):
                if money_shop >= 50:
                    return 'double_shot'
                else:
                    button_surface6.blit(text6, text_rect6)
                    screen.blit(button_surface6, (button_rect6.x, button_rect6.y))

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 298, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 300, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 298, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 298, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 298, 10), 2)

    if button_rect2.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface2, (127, 255, 212), (1, 1, 298, 48))
    else:
        pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 300, 50))
        pygame.draw.rect(button_surface2, (255, 255, 255), (1, 1, 298, 48))
        pygame.draw.rect(button_surface2, (0, 0, 0), (1, 1, 298, 1), 2)
        pygame.draw.rect(button_surface2, (0, 100, 0), (1, 48, 298, 10), 2)

    if button_rect3.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface3, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface3, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface3, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface3, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface3, (0, 100, 0), (1, 48, 148, 10), 2)

    if button_rect4.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface4, (127, 255, 212), (1, 1, 298, 48))
    else:
        pygame.draw.rect(button_surface4, (0, 0, 0), (0, 0, 300, 50))
        pygame.draw.rect(button_surface4, (255, 255, 255), (1, 1, 298, 48))
        pygame.draw.rect(button_surface4, (0, 0, 0), (1, 1, 298, 1), 2)
        pygame.draw.rect(button_surface4, (0, 100, 0), (1, 48, 298, 10), 2)

    button_surface.blit(text1, text_rect)
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    button_surface2.blit(text2, text_rect2)
    screen.blit(button_surface2, (button_rect2.x, button_rect2.y))

    button_surface3.blit(text3, text_rect3)
    screen.blit(button_surface3, (button_rect3.x, button_rect3.y))

    button_surface4.blit(text4, text_rect4)
    screen.blit(button_surface4, (button_rect4.x, button_rect4.y))

    button_surface5.blit(text5, text_rect5)
    screen.blit(button_surface5, (button_rect5.x, button_rect5.y))

    pygame.display.update()

