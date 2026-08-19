"""1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.
"""

def cargar():
    temperaturas=[]
    for i in range (6):
        temp=float(input(F"Ingrese la temperatura de la hora {i+1}"))
        temperaturas.append(temp)

    return temperaturas

def procesar(temperaturas):
    max=temperaturas[0]
    min=temperaturas[0]
    for i in range(len(temperaturas)):
        if max<temperaturas[i]:
            max=temperaturas[i]
        if min>temperaturas[i]:
            min=temperaturas[i]  
    extremos=(max,min)
    return extremos          


temperaturas=cargar()
max,min=procesar(temperaturas)
print(F"La temperatura maxima es de {max}")
print(F"La temperatura minima es de {min}")