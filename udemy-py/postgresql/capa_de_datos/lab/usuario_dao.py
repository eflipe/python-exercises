from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log


class UsuarioDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios.')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.usuario, persona.password, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    persona1 = Usuario(nombre='Alejandra', apellido='Tellez', email='atellez@mail.com')
    personas_insertadas = UsuarioDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

    # Actualizar un registro
    persona1 = Usuario(1,'Juan', 'Perez', 'jperez@mail.com')
    personas_actualizadas = UsuarioDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Eliminar un registro
    persona1 = Usuario(id_persona=15)
    personas_eliminadas = UsuarioDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # Seleccionar objetos
    personas = UsuarioDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
