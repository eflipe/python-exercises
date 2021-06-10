from logger_base import log


class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None, year=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__year = year

    def __str__(self):
        return f'''
                ID persona: {self.__id_persona}, Nombre: {self.__nombre},
                Apellido: {self.__apellido}, Email: {self.__email}
                '''

    @property
    def id_persona(self):
        return self.__id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self.__id_persona = id_persona

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


if __name__ == '__main__':
    obj_persona_1 = Persona(1, "Pepe", "Pernorilli", "kjjjj@hotmail.com")
    log.debug(obj_persona_1)
