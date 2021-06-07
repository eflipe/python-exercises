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
            sentencia = 'INSERT INTO api_app_pictures(autor, titulo, url_pic, year) VALUES(%s, %s, %s, %s)'
            valores = (
                    ('Pepe FOTO', 'Titulo mágico', 'https://pbs.twimg.com/media/Eb31bEtXkAAoa0p?format=jpg&name=large', 1994),
                    ('Pepe 2' , 'Titulo mágico 2', 'https://pbs.twimg.com/media/Eb31bEtXkAAoa0p?format=jpg&name=large', 1995),
                    ('Pepe 3', 'Titulo mágico 3', 'https://pbs.twimg.com/media/Eb31bEtXkAAoa0p?format=jpg&name=large', 1998)
                    )
            cursor.executemany(sentencia, valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Tenemos un error: {e}')

finally:
    conexion.close()
