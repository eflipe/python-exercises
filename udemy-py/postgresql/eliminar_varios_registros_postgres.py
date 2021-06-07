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
            sentencia = "DELETE FROM api_app_pictures WHERE id IN %s"
            entrada = "29,30,31"
            print(entrada.split(','))
            valores = (tuple(entrada.split(',')))
            cursor.executemany(sentencia, valores)
            registros_actuaizados = cursor.rowcount
            print(f'Registros insertados: {registros_actuaizados}')
except Exception as e:
    print(f'Tenemos un error: {e}')

finally:
    conexion.close()
