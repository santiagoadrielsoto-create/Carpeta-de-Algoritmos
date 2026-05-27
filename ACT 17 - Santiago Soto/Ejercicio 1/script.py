"""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50
del primer elemento de &quot;lista&quot;.
Volver a imprimir la lista.
"""
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

acumulador = [] 

for x in range(1):
        for j in range(len(lista[0])):
            if lista[0][j] > 50:
                acumulador.append(lista[0][j])
            else:
                lista[-1].append(lista[0][j])
        lista[0] = []

for x in range(len(lista)):
    sublista_limpia = []

    for j in range(len(lista[x])):
        if lista[x][j] > 50:
            acumulador.append(lista[x][j])
        else:
            sublista_limpia.append(lista[x][j])
    lista[x] = sublista_limpia

for numero in range (len(acumulador)):
    lista[0].append(acumulador[numero])

print("Resultado:", lista)