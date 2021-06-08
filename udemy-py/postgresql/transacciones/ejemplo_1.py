import psycopg2 as bd

conexion = bd.connect(user='postgres',
           password='postgres',
           host='127.0.0.1',
           port='5432',
           database='postgres')

try:
    # crear varias secuencias que modifique el estado de la BD
    conexion.autocommit = False

    cursor = conexion.cursor()
    
    sentencia = 'INSERT INTO api_app_pictures(autor, titulo, url_pic, year) VALUES(%s, %s, %s, %s)'
    valores = ('New Pepe FOTO 2', 'Titulo mágico', 'https://pbs.twimg.com/media/Eb31bEtXkAAoa0p?format=jpg&name=large', 1994)
    cursor.execute(sentencia, valores)

    sentencia = "UPDATE api_app_pictures SET autor=%s, titulo=%s WHERE id=%s"
    valores = ('MODIFICADO PEPE 32', "Nuevo titulo", 32)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print("Todo commiteado.")

except Exception as e:
    conexion.rollback()
    print(f'Tenemos un error, se hizo rollaback: {e}')

finally:
    conexion.close()
