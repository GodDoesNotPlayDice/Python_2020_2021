import sqlite3 #Importar sqlite
conexion = sqlite3.connect('pruebas.db') # Nombre de la base de datos

#Crear cursor
cursor = conexion.cursor()
#Consulta 
consulta = conexion.cursor()
sql = """
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
"""
#Crear tabla
cursor.execute(sql)
'''
# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
'''



productos = [
    ('Ordenador portatil', 'Buen PC', 700),
    ('Telefono movil', 'Buen PC', 140),
    ('Placa basae', 'Buen PC', 80),
    ('Tablet 15', 'Buena tablet', 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()
# Update
cursor.execute("UPDATE productos SET precio=670 WHERE precio=80 ")
#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()
for producto in productos:
    print(f'''
    ID: {producto[0]} 
    Titulo: {producto[1]} 
    Descripcion: {producto[2]} 
    Precios: {producto[3]} 
    
    ''')

    #Listar el primer registro
cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)
#Borrar registros
cursor.execute('DELETE FROM productos')
conexion.commit()

#Guardar
conexion.commit()

conexion.close() # Cerrar la base de datos