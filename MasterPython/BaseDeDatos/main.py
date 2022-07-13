import mysql.connector

# Conexion
database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='master_python'
)
# Comprobar conexion
# print(database)
#Cursor
cursor = database.cursor(buffered=True) #buffered es para que al ejecutar muchas consultas no nos falle
#Crear base de datos
cursor.execute('CREATE DATABASE IF NOT EXISTS master_python')
#Mostrar base de datos
# cursor.execute('SHOW DATABASES')
# for bd in cursor:
#     print(bd)

#Crear Tablas
sql = """
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculos PRIMARY KEY(id)
)
"""
cursor.execute(sql)
#Mostar tablas

# cursor.execute("SHOW TABLES")
# for table in cursor:
#     print(table)

# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)
]
# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
# database.commit()
#Listar
cursor.execute("SELECT * FROM vehiculos")
resutl = cursor.fetchall()
for coche in resutl:
    print(coche)
cursor.execute('SELECT * FROM vehiculos')
# Muestra el primero
coche = cursor.fetchone()
# print(coche)
#Borrar registros de la base de datos
# cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
# database.commit()
# print(cursor.rowcount, "borrados!")
# Actualizar
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
print(cursor.rowcount, "Actualizado")
database.commit()
database.close()