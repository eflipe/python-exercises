import psycopg2

conexion = psycopg2.connect(user='postgres',
           password='postgres',
           host='127.0.0.1',
           port='5432',
           database='postgres')

print(conexion)

try:
    with conexion:
        # Cursor: permite ejecutar sentencias SQL
        with conexion.cursor() as cursor:
            sentencia = "UPDATE api_app_pictures SET autor=%s, titulo=%s WHERE id=%s"
            valores = (
            ('UPDATE PEPE 31', "Nuevo titulo", 31),
            ('UPDATE PEPE 30', "Nuevo titulo", 30),
            ('UPDATE PEPE 29', "Nuevo titulo", 29)
            )
            cursor.executemany(sentencia, valores)
            registros_actuaizados = cursor.rowcount
            print(f'Registros insertados: {registros_actuaizados}')
except Exception as e:
    print(f'Tenemos un error: {e}')

finally:
    conexion.close()
