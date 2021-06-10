# DAO: data access object. Es un patrón de diseño para comunicarse con una # DEBUG:
from conexion_db import ConexionDB
from persona_class import Persona
from logger_base import log


class PersonaDAO:
    """
    Data access object
    CRUD
    """
    _SELECCIONAR = 'SELECT * FROM api_app_pictures ORDER BY id'
    _INSERTAR = 'INSERT INTO api_app_pictures(autor, titulo, url_pic, year) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE api_app_pictures SET autor=%s, titulo=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM api_app_pictures WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with ConexionDB.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)

            return personas

    @classmethod
    def insertar(cls, persona):
        with ConexionDB.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.year)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Dato a insertados: {persona}')
                return cursor.rowcount


if __name__ == '__main__':
    # insertar
    persona_1 = Persona(nombre="DAO PEPE", apellido="ALGO0", email="DDD", year=2)
    personas_insert = PersonaDAO.insertar(persona_1)
    log.debug("INSERT: {personas_insert}")

    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
