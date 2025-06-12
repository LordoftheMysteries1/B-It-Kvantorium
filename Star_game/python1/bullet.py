import pygame

class Bullet(pygame.sprite.Sprite):
    def _＿init＿_(self, screen, ship, bullet_width, speed_bullet, double_shot_pause):
        """
        screen - экран на котором отрисовывается пуля
        ship - объект из которго вылетает пуля
        """
        super(Bullet, self).__init__()#наследуем инициализацию у родителя
        self.screen = screen
        self.rect = pygame.Rect(0, 0, bullet_width, 15) #x y w h
        self.color = 0, 255, 255
        self.speed = 6 + speed_bullet
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y) - double_shot_pause


    def rendering(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update_pos(self):
        self.y -= self.speed
        self.rect.y = self.y
    
    