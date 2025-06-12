import pygame
import sys



def settings(screen):
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Громкость', 1, (180, 0, 0))
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
                return True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect2.collidepoint(event.pos):
                return 'exit'

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

