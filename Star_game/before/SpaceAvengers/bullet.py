import pygame

class Bullet(pygame.sprite.Sprite):
    def _＿init＿_(self, screen, ship):
        """
        screen - экран на котором отрисовывается пуля
        ship - объект из которго вылетает пуля
        """
        super(Bullet, self).__init__()#наследуем инициализацию у родителя
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 12) #x y w h
        self.color = 168, 230, 29
        self.speed = 1
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)


    def rendering(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update_pos(self):
        self.y -= self.speed
        self.rect.y = self.y
    
    