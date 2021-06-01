# sobre escribimos la clase Exception

class ErrorNumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje
