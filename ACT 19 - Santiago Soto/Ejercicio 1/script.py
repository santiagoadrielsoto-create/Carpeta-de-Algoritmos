"""
1. Crear una lista de enteros por asignación. Definir una función que reciba
una lista de enteros y un segundo parámetro de tipo entero. Dentro de la
función mostrar cada elemento de la lista multiplicado por el valor entero
enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)
"""

def multiplicar():
    lista=[2,3,8,10,20]
    a=4
    multiplicacion=[]
    for i in range(len(lista)):
        lista[i]=lista[i]*a
        multiplicacion.append(lista[i])
        print(F"El Numero de la lista es {lista[i]} y multiplicado por 4 es {multiplicacion[i]}")

multiplicar()