import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd= '',
    database='asistente'
)
cursor = dataBase.cursor(buffered=True)
cursor.execute('CREATE DATABASE IF NOT EXISTS asistente')
sql = '''
CREATE TABLE IF NOT EXISTS datos(
    id int(20) auto_increment not null,
    usuario varchar(15) not null,
    password varchar(10) not null,
    CONSTRAINT pk_asistente PRIMARY KEY(id)
)
'''
cursor.execute(sql)
def getInfo(user,password):
    cursor.execute(f"INSERT INTO datos VALUES(null, {user}, {password})")

dataBase.commit()
dataBase.close()
