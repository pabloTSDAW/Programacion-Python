import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Crea la tabla
c.execute('''CREATE TABLE contactos
             (usuario text, telefono text, email text)''')

# Inserta una fila de datos
c.execute('''INSERT INTO contactos VALUES ('pablo','661155196','pablo@gmail.com'),
          ('carlos','661155193','carlos@gmail.com'), ('tomy','678075731','tomy@gmail.com')''')
# Guarda (commit) los cambios
conn.commit()

# Cerramos la conexción.
# Tienes que estar seguro de que los cambios se han guardado antes de cerrar
# o se perderán.
'''conn.close()'''


#Ejecutar por separado
for row in c.execute('SELECT * FROM contactos'):
        print(row)









