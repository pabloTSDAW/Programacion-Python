'''Crear una clase Cromo (id, nombre, imagen) y otra Album,
hacer el Album (diccionario de cromos) iterable. Crear métodos para
añadir cromos al álbum…'''

class Cromo:
    def __init__(self, id, nombre, imagen):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen

    def __str__(self):
        return 'Cromo({},{},{})'.format(self.id, self.nombre, self.imagen)


class Album:
    def __init__(self):
        self.dic = {}
        self.i = 0

    def añadircromo(self, cromo):
        '''Añade un cromo al album'''
        self.dic[cromo.id] = cromo

    def obtenercromo(self, numero):
        '''Devuelve un cromo identificado por numero'''
        return self.dic[numero]

    def __next__(self):
        '''Devuelve el siguiente elemento del Album'''
        codigos = list(self.dic.keys())
        codigos.sort()
        estampitas = list(self.dic.values())
        if self.i < len(codigos):
            n = self.i
            self.i += 1
            return self.dic[codigos[n]]
        else:
            raise StopIteration

    def __iter__(self):
        return self

messi = Cromo(1, 'Messi', 'Barça')
cristiano = Cromo(2, 'Cristiano', 'Piscina')
neymar = Cromo(3, 'Neymar', 'Juzgado')

a = Album()

a.añadircromo(messi)
a.añadircromo(cristiano)
a.añadircromo(neymar)

##for c in a:
##    print(c)
        
