import sys

from settings import Settings

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
        # Color del fondo


    def run_game(self):
        """Iniciando el loop principal del juego."""
        while True:
            # Espero los eventos del mouse y el teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Re-dibujar la pantalla en cada loop
            self.screen.fill(self.settings.bg_color)

            # Dibuja la pantalla más reciente
            pygame.display.flip()


if __name__ == '__main__':
    # Crea una instancia del juego, y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
