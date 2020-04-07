from random import choice


class RandomWalk:
    """Generador de random walks"""

    def __init__(self, num_points=5000):
        """Atributos iniciales"""
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos los puntos del random walk"""

        while len(self.x_values) < self.num_points:
            # Decide a cuál dirección ir y en cuánta distancia
            # derecha(1) o izquierda (-1)
            x_direction = choice([1, -1])
            # qué tan lejos ir
            x_distance = choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            # arriba o abajo
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            # Movimiento que no van a ningún lugar
            if x_step == 0 and y_step == 0:
                continue
            # Calcula nueva posicion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
