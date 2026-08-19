"""
3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ [&quot;Franco&quot;, (78.5, 77.2, 79.1)], [&quot;Lewis&quot;, (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
"""

def cargar():
    pilotos=[]
    for i in range(4):
        nombre=input(F"Ingrese el nombre del piloto {i+1}")
        tiempos=[]
        for j in range(3):
            temp=float(input(F"Ingrese el tiempo en la vuelta {j+1}"))
            tiempos.append(temp)
        pilotos.append([nombre,tiempos])
    return pilotos

def promedios(pilotos):
    for i in range(len(pilotos)):
        nombre=pilotos[i][0]
        t1,t2,t3 = pilotos[i][1]

        promedio=(t1+t2+t3)/3
        print(F"El promedio de tiempo del piloto {nombre} es de {promedio}")

def mejor_vuelta(pilotos):
    mejor=pilotos[0][1][0]
    c=0
    for i in range(len(pilotos)):
        for j in range(3):
            if pilotos[i][1][j]<mejor:
                mejor=pilotos[i][1][j]
                c=i
    print(F"La vuelta mas rapida fue {mejor} y fue del piloto {pilotos[c][0]}")

pilotos=cargar()
promedios(pilotos)
mejor_vuelta(pilotos)