'''a) Escribir una función a la que se le pasa un número de cliente y produce
un listado con la lista de los pedidos de ese cliente con la fecha y la
cuantía de cada uno. Que produzca también la diferencia entre el total
de pagos y total de pedidos, si está al corriente de sus pagos.'''

import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='654321', host='localhost',
                              database='classicmodels')

c = cnx.cursor()
cnx.commit()


def pedidos(idcliente):
    return c.execute('SELECT customers.customerNumber, orders.orderNumber, \
            orders.orderDate, orderdetails.priceEach * orderdetails.quantityOrdered \
            as cuantia  FROM customers\
            JOIN orders on customers.customerNumber = orders.customerNumber\
            JOIN orderdetails on orderdetails.orderNumber = orders.orderNumber\
            WHERE customers.customerNumber = {}'.format(idcliente))

def pagos(idcliente):
    return c.execute('SELECT SUM(payments.amount) FROM payments\
                      WHERE customerNumber = {}'.format(idcliente))


def deudor(idcliente):
    pedidos(idcliente)
    lista = []
    lista2 = []
    for row in c:
        fila = list(row)
        lista.append(fila[3])
    debe = sum(lista)
    pagos(idcliente)
    for row2 in c:
        lista2 = list(row2)
        pago = sum(lista2)
        if pago >= debe:
            print('El cliente {} ha pedido {} € en productos y ha pagado {} €, por lo que está al corriente de pago'.format(idcliente, debe, pago))
        else:
            print('El cliente {} ha pedido {} € en productos y ha pagado {} €, por lo que NO está al corriente de pago'.format(idcliente, debe, pago))
    

#deudor(103)


'''b) Hacer el informe anterior extensible a una lista de clientes.'''

def lista_clientes():
    return c.execute('SELECT distinct customerNumber FROM customers')

def deudores():
    lista_clientes()
    lista = []
    clientes = []
    for row in c:
        lista = list(row)
        idcliente = lista[0]
        clientes.append(idcliente)
    return clientes

##for i in deudores():
##    deudor(i)

for i in deudores():
    try:
        deudor(i)
    except TypeError as error:
        print(error)




