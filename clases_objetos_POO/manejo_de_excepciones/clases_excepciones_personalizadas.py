class NumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        # Exception, la clase padre, tiene el atributo message
        self.message = mensaje
