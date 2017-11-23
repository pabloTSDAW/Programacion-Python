'''Vamos a construir la clase coleccionClientes con la estructura dada
(atributo:dic_cliente diccionario con el numCliente y Cliente, obtendrá todos
los clientes, tendrá como métodos cargar_clientes(), tendrá también la
responsabilidad de guardar los nuevos clientes que se creen en la base
de datos, dicho método se llamará nuevo_cliente(numCliente,nombre,teléfono,email)
y también tendrá el método modificar_cliente(numCliente,datos que necesite ser
modificados poniendo nombre del campo=valor.)). Crear las clases Cliente
y ControlBD (que interactúa solo con la base de datos, solo devuelve un
cursor, las otras clases no manejan base de datos).'''

import mysql.connector



class Cliente:
    def __init__(self, numCliente, nombre, direccion, telefono):
        self.numCliente = numCliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return 'Cliente({},{},{},{})'.format(self.numCliente, self.nombre, self.direccion, self.telefono)


class ColeccionClientes:
    def __init__(self):
        self.dic_clientes = {}
        self.bd = ControlBD()
        self.bd.conectar()

    def obtener_cliente(self, numCliente):
        '''Muestra el cliente identificado por numCliente'''
        self.bd.obtener_clienteBD(numCliente)
        datos = self.bd.cur.fetchone()
        numCliente, nombre, direccion, telefono = datos
        return Cliente(numCliente, nombre, direccion, telefono)
        

    def imprimir_clientes(self):
        '''Imprime el diccionario de clientes'''
        for cliente in self.dic_clientes:
            print(self.dic_clientes[cliente])

    def carga_clientes(self):
        '''Guarda los clientes de la base de datos en un diccionario'''
        self.bd.ver_contactos()
        for row in self.bd.cur:
            #cliente = Cliente(row[0], row[1], row[2], row[3])
            numCliente, nombre, direccion, telefono = row
            self.dic_clientes[numCliente] = Cliente(numCliente, nombre, direccion, telefono)
        return self.dic_clientes

    def crear_cliente(self, numero, nombre, direccion, telefono):
        '''Inserta una nuevo Cliente en la base de datos'''
        try:
            cliente = Cliente(numero, nombre, direccion, telefono)
            self.bd.meter_cliente(cliente)
        except Exception as error:
            print(error)


class ControlBD:
    def __init__(self):
        self.conexion = None
        self.cur = None
   
    def conectar(self):
        '''Conecta con la base de datos'''
        cnx = mysql.connector.connect(user='root',
                              password='654321', host='localhost',
                              database='classicmodels')
        self.conexion = cnx
        self.cur = cnx.cursor()

    def obtener_clienteBD(self, numero):
        return self.cur.execute('''
        SELECT customerNumber, customerName, city, phone
        FROM customers WHERE customerNumber = {}'''.format(numero))
        
    def ver_contactos(self):
        return self.cur.execute('''
        SELECT customerNumber, customerName, city, phone
        FROM customers''')

    def meter_cliente(self, cliente):
        return self.cur.execute('''
        INSERT INTO customers(customerNumber, customerName, city, phone)
        VALUES({},{},{},{})'''.format(cliente.numCliente, cliente.nombre, cliente.direccion, cliente.telefono))
        self.conexion.commit()
                         
                

col = ColeccionClientes()
col.carga_clientes()
col.crear_cliente(501, 'Pablo', None, '661155196')
##col.imprimir_clientes()
print(col.obtener_cliente(501))



