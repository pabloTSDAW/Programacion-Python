CREATE DATABASE proyecto;

USE proyecto;

DROP TABLE es_repuesto;
DROP TABLE contiene;
DROP TABLE encargo;
DROP TABLE compra;
DROP TABLE trabajador;
DROP TABLE proveedor;
DROP TABLE cash;
DROP TABLE Stock;
DROP TABLE producto;
DROP TABLE ClienteNoRegistrado;
DROP TABLE clienteregistrado;


CREATE TABLE ClienteRegistrado
(
Nombre varchar(20) PRIMARY KEY,
Telefono varchar(9)
);


CREATE TABLE ClienteNoRegistrado
(
Fecha date
);


CREATE TABLE `Producto`
(
`Ref` int PRIMARY KEY,
`Nombre` varchar(50),
`Descripción` varchar(50),
`PrecioUnidad` float,
`Tipo` varchar(20),
`Unidades` int
);


CREATE TABLE Stock
(
RefProducto int,
Unidades int,
PRIMARY KEY (RefProducto, Unidades),
FOREIGN KEY (RefProducto) REFERENCES Producto(Ref)
);


DROP TABLE IF EXISTS Cash;

CREATE TABLE Cash
(
Codigo int PRIMARY KEY,
Nombre varchar(20)
);


DROP TABLE IF EXISTS Proveedor;

CREATE TABLE Proveedor
(
Codigo int PRIMARY KEY,
Nombre varchar(20),
Telefono varchar(9)
);


DROP TABLE IF EXISTS Trabajador;

CREATE TABLE Trabajador
(
DNI int PRIMARY KEY,
Nombre varchar(20)
);


DROP TABLE IF EXISTS Compra;

CREATE TABLE Compra
(
Numero int PRIMARY KEY,
Total float
);


DROP TABLE IF EXISTS Encargo;

CREATE TABLE Encargo
(
NumeroPedido int PRIMARY KEY,
NombreCliente varchar(20),
NumeroCompra int,
FOREIGN KEY (NombreCliente) REFERENCES ClienteRegistrado(Nombre),
FOREIGN KEY (NumeroCompra) REFERENCES Compra(Numero)
);


DROP TABLE IF EXISTS Contiene;

CREATE TABLE Contiene
(
NumeroPedido int,
RefProducto int,
PRIMARY KEY (RefProducto, NumeroPedido),
FOREIGN KEY (RefProducto) REFERENCES Producto(Ref),
FOREIGN KEY (NumeroPedido) REFERENCES Encargo(NumeroPedido)
);


DROP TABLE IF EXISTS Es_repuesto;

CREATE TABLE Es_repuesto
(
RefProducto int,
Unidades int,
CodigoCash int,
CodigoProveedor int,
DiaReposicion varchar(10),
PRIMARY KEY (RefProducto, Unidades),
FOREIGN KEY (RefProducto, Unidades) REFERENCES Stock(RefProducto, Unidades),
FOREIGN KEY (CodigoCash) REFERENCES Cash(Codigo),
FOREIGN KEY (CodigoProveedor) REFERENCES Proveedor(Codigo)
);


/*INSERT*/

INSERT INTO ClienteRegistrado VALUES
('Pepa', '664221435'), ('Antonio', '958121416'), ('Juana', '669877455'), ('Piedad', '856224153'),
('Jacinto', '662334578'), ('Lucia', '958151477'), ('Antonia', '662334587'), ('Francisco', '756224897'),
('Laura', '958664475'), ('Mario', '958368697'), ('Eduardo', '958785514'), ('Daniel', '958224989'),
('Maria', '667889989');


INSERT INTO ClienteNoRegistrado VALUES
('2017-02-27'), ('2017-03-01'), ('2017-03-03'), ('2017-03-06'), ('2017-03-08'), ('2017-03-10'),
('2017-03-10'), ('2017-03-15'), ('2017-03-17'), ('2017-03-18'), ('2017-03-20'), ('2017-03-21'),
('2017-03-22');


INSERT INTO Producto VALUES
(15, 'Choped barra', 'Choped', 4.80, 'Embutido', 3), (58, 'Huevos de codorniz', 'Huevos', 1.30, 'Varios', 10),
(57, 'Huevos de corral', 'Huevos', 1.50, 'Varios', 10), (54, 'Pastel de manzana', 'Pastel de manzana', 4.50, 'Varios', 30),
(55, 'Turrón de Estepa', 'Turrón duro', 1.10, 'Varios', 30), (32, 'Lomo embuchado', 'Lomo', 4.30, 'Embutido', 2),
(47, 'Chorizo extra picante', 'chorizo picante', 2.30, 'Embutido', 3), (21, 'Jamón ibérico', 'Jamón', 3.20, 'Embutido', 10),
(12, 'Salchichas alemanas', 'Salchichas', 2, 'Embutido', 4), (14, 'Mortadela con Aceitunas', 'Mortadela', 2.30, 'Embutido', 3);


INSERT INTO Stock VALUES
(15, 3), (58, 10), (57, 10), (54, 30), (55, 30), (32, 2), (47, 3), (21, 10), (12, 4), (14, 30);


INSERT INTO Cash VALUES
(1, 'Supersol'), (2, 'AhorraFresh'), (3, 'Freshco');


INSERT INTO Proveedor VALUES
(1, 'Antonio Carnes', '662355886'), (2, 'Juan Embutidos', '958744447'), (3, 'Felipe Varios', '663225522');


INSERT INTO Trabajador VALUES
(77140658, 'Salvador');


INSERT INTO Compra VALUES
(1, 14.50), (2, 3.40), (3, 5.50), (4, 1.20), (5, 2.20), (6, 12.30), (7, 8.30),
(8, 2.58), (9, 10.20), (10, 5.50), (11, 6.20), (12, 7.60), (13, 9.0);


INSERT INTO Encargo VALUES
(1, 'Pepa', 1), (2, 'Antonio', 2), (3, 'Juana', 3), (4, 'Piedad', 4), (5, 'Jacinto', 5), (6, 'Lucia', 6),
(7, 'Antonia', 7), (8, 'Francisco', 8), (9, 'Laura', 9), (10, 'Mario', 10), (11, 'Eduardo', 11), (12, 'Daniel', 12),
(13, 'Maria', 13);


INSERT INTO Contiene VALUES
(1, 15), (2, 58), (3, 57), (4, 54), (5, 55), (4, 32), (7, 47), (8, 21), (9, 54), (1, 12), (8, 14), (5, 32), (7, 14);



INSERT INTO Es_repuesto VALUES
(15, 5, NULL, 2, 'Jueves'), (58, 5, 2, NULL, NULL), (57, 5, 2, NULL, NULL), (54, 30, NULL, 3, 'Miercoles'),
(55, 10, NULL, 3, 'Miercoles'), (32, 4, NULL, 1, 'Lunes'), (47, 5, NULL, 2, 'Jueves'), (21, 5, 1, NULL, 'Lunes'),
(12, 5, 3, NULL, NULL), (14, 3, NULL, 2, 'Jueves');




SELECT * FROM clienteregistrado;
SELECT * FROM clientenoregistrado;
SELECT * FROM producto;
SELECT * FROM stock;
SELECT * FROM cash;
SELECT * FROM proveedor;
SELECT * FROM trabajador;
SELECT * FROM compra;
SELECT * FROM encargo;
SELECT * FROM contiene;
SELECT * FROM es_repuesto;


INSERT INTO producto VALUES(200, 'pepsi', 'zero', 5, 'bebida', 5);
SELECT * FROM producto WHERE ref = 200;
DELETE FROM producto WHERE ref = 200;

