import pygame


class Ship:
    """Control de la nave espacial"""

    def __init__(self, ai_game):
        """Inicializar la nave en posición inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Cargar la imagen de la nave
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Cada nueva nave comienza en la mitad-baja de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        # Posiciones decimales
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posicion de la nave según el valor del Flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Dibuja la nave en posición actual"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
