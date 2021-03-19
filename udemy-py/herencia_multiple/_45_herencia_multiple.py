# figura geometrica
# ABC = Abstract Base class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    # GET / SET
    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def get_alto(self):
        return self.__alto

    def set_alto(self, alto):
        self.__alto = alto

    @abstractmethod
    def area():
        pass

    def __str__(self):
        return "Ancho: "+ str(self.get_ancho()) + ", Alto: "+ str(self.get_alto())
