import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Comportamiento general del juego"""
    def __init__(self):
        """Initializa el juego"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((
                                     self.settings.screen_width,
                                     self.settings.screen_height))
        pygame.display.set_caption("Invasión Extraterrestre")
        self.ship = Ship(self)
        self.bullets = Group()
        self.aliens = Group()

        self._create_fleet()

    def run_game(self):
        """Iniciando el loop principal del juego."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        # Espero los eventos del mouse y el teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Mueve la nave a la derecha
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Mueve la nave a la izquierda
            self.ship.moving_left = True
            # Salir con la latra Q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Detiene el movimiento
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Detiene el movimiento
            self.ship.moving_left = False

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        # Re-dibujar la pantalla en cada loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Dibuja los Disparos
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Dibuja la pantalla más reciente
        pygame.display.flip()


if __name__ == '__main__':
    # Crea una instancia del juego, y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
