import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
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

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
conn.commit()
cursor.execute("SELECT * FROM productos")
prod = cursor.fetchall()
print(prod)


