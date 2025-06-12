import pygame


class enemy_Bullet(pygame.sprite.Sprite):
    def _＿init＿_(self, screen, ship):
        """
        screen - экран на котором отрисовывается пуля
        ship - объект из которго вылетает пуля
        """
        super(enemy_Bullet, self).__init__()  # наследуем инициализацию у родителя

        self.screen = screen
        self.rect = pygame.Rect(0, 0, 20, 15)  # x y w h
        self.color = 255, 0, 0
        self.speed = 6
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.bottom
        self.y = float(self.rect.y)

    def rendering(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update_pos(self):
        self.y += self.speed
        self.rect.y = self.y
