'''Buscar los usuarios actuales de la base de datos y los privilegios
que tiene. Dentro de mysql hay una base de datos llamada mysql (no tocarla).
Listar las tablas propias de mysql.'''

import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='654321', host='localhost',
                              database='mysql')

c = cnx.cursor()
cnx.commit()

def usuarios():
    return c.execute('SELECT * FROM user')

def ver_tabla():
    return c.execute('DESCRIBE user')

#ver_tabla()
usuarios()
for row in c:
    print(row)
