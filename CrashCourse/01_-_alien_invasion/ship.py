import pygame


class Ship:
    """Control de la nave espacial"""

    def __init__(self, ai_game):
        """Inicializar la nave en posición inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Cargar la imagen de la nave
        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()

        # Cada nueva nave comienza en la mitad-baja de la pantalla
        self.image_rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posicion de la nave según el valor del Flag"""
        if self.moving_right:
            self.image_rect.x += 1
        if self.moving_left:
            self.image_rect.x -= 1

    def blitme(self):
        """Dibuja la nave en posición actual"""
        self.screen.blit(self.image, self.image_rect)
