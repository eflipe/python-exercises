from random import randint


class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Dado de 6 lados"""
        self.num_sides = num_sides

    def roll(self):
        """Genera un número random entre 1 y num_sides"""
        return randint(1, self.num_sides)
