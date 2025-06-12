import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Boss, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/boss.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 1

    def rendering(self):
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        if self.rect.x > 325:
            self.speed *= -1
        if self.rect.x < 50:
            self.speed *= -1
        self.x += self.speed
        self.rect.x = self.x