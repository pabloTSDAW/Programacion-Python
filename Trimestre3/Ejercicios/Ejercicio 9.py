'''a) Sacar un listado de todas las tablas que tiene la base de
datos example. (SHOW TABLES)'''

import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='654321', host='localhost',
                              database='classicmodels')

c = cnx.cursor()
cnx.commit()

def ver_tablas():
    return c.execute('SHOW TABLES')


#Llamar a la función antes de recorrer el cursor!!!
##ver_tablas()
##for row in c:
##    print(row)
    

'''b) Sacar una lista de todos los clientes españoles (nombre,
numero, teléfono, ciudad y país).'''

def clientes_spain():
    return c.execute("SELECT customerNumber, customerName, phone, city, country FROM customers WHERE country = 'Spain'")


##clientes_spain()
##for row in c:
##    print(row)


'''c) Imprimir todos los pedidos de un cliente (dado el número de un
cliente). Mostrar orderNumber, productCode, productName, cantidad, precio
unitario y del producto productName y productCode El programa tiene que
calcular el total de líneas, el subtotal del pedido (precio por línea) y
el total de todos los pedidos.'''

def pedidos(idcliente):
    return c.execute('SELECT orderLineNumber, orders.orderNumber, orderdetails.productCode, quantityOrdered, priceEach, productName\
                       FROM orderdetails\
                        JOIN products on products.productCode = orderdetails.productCode\
                        JOIN orders on orders.orderNumber = orderdetails.orderNumber\
                        WHERE orders.customerNumber = {}\
                        GROUP BY orderNumber\
                         ORDER BY orderLineNumber'.format(idcliente))
        

def resumen_pedidos(idcliente):
    try:
        pedidos(idcliente)
        lista = []
        total = []
        for row in c:
            fila = list(row)
            print('Total línea: ', fila[0], ':', fila[3] * fila[4], '€')
            total.append(fila[3] * fila[4])
            lista.append(row)
        print('Pedidos: ',len(lista), '- Total: ', sum(total), '€')
    except Exception as error:
        print('Error producido: ', error)


resumen_pedidos(172)


