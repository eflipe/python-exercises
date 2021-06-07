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
            sentencia = "DELETE FROM api_app_pictures WHERE id=%s"
            valores = (31,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Tenemos un error: {e}')

finally:
    conexion.close()
