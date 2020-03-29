import sys

from settings import Settings
from ship import Ship

import pygame


class AlienInvasion:
    """Comportamiento general del juego"""#
    def __init__(self):
        """Initializa el juego"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((
                                     self.settings.screen_width,
                                     self.settings.screen_height))
        pygame.display.set_caption("Invasión Extraterrestre")
        self.ship = Ship(self)

    def run_game(self):
        """Iniciando el loop principal del juego."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Espero los eventos del mouse y el teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Re-dibujar la pantalla en cada loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Dibuja la pantalla más reciente
        pygame.display.flip()



if __name__ == '__main__':
    # Crea una instancia del juego, y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
