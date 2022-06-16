class ClaseAritmetica:
    '''
    Clase Aritmetica para realizar las operaciones sumar, restar, etc
    '''

    def __init__(self, operando_a, operando_b):
        self.operando_a = operando_a
        self.operando_b = operando_b

    # en el metodo sumar usamos los atributos self.operando_a y self.operando_b
    def sumar(self):
        return self.operando_a + self.operando_b

    def restar(self):
        return self.operando_a - self.operando_b

    def multiplicar(self):
        return self.operando_a * self.operando_b

    def dividir(self):
        return self.operando_a / self.operando_b


obj_aritmetica = ClaseAritmetica(5, 6)
print(obj_aritmetica.sumar())
print(obj_aritmetica.restar())
print(obj_aritmetica.multiplicar())
print(f'Division: {obj_aritmetica.dividir():.2f}')
