

def rotarlista(lista, n=1):
    lista2 = lista[n:] + lista[:n]
    return lista2


def rotar(str,n):
    rotada=""
    rotada = str[n:] + str[:n]
    return rotada

rotar('ramo', 1)



def anagramas(palabra):
    lista2 = []
    lista = list(palabra)
    for k in range(len(lista)):
        for i in lista:
            saca = lista.pop()
            for j in range(len(lista)):
                rotarlista(lista, 1)
                lista.insert(0, saca)
            lista2.append(lista)
            print(lista2)
        
        


'''anagramas('ramo')'''
    



