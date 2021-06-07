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
            sentencia = 'SELECT * FROM api_app_pictures'
            # sentencia = "SELECT * FROM api_app_pictures WHERE autor = 'Ruth Marten'"
            # sentencia = "SELECT * FROM api_app_pictures WHERE id = %s"
            # sentencia = "SELECT * FROM api_app_pictures WHERE id IN %s"
            llaves_primarias = ((1, 2, 3, 4), )
            id = 4
            # llaves_primarias = input("Ingresa valores separados por coma: ")
            # llaves_primarias = (tuple(llaves_primarias.split(',')),)  # tupla de tuplas
            # sentencia = 'SELECT nombre, email FROM persona'
            # cursor.execute(sentencia, (id,))
            cursor.execute(sentencia, llaves_primarias)

            registros = cursor.fetchall()

            # registros = cursor.fetchone()
            print(registros) # es una lista que contiene tuplas
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Error: {e}')

finally:
    conexion.close()
