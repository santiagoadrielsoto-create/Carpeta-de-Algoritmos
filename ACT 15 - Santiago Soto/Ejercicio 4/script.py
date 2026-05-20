"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
"""

lista=[]

for i in range(5):
    num=int(input(f"Ingrese un numero entero en la posicion {i+1}"))
    lista.append(num)

for i in range(4):
    for k in range(4-i):
        if lista[k]>lista[k+1]:
            aux=lista[k]
            lista[k]=lista[k+1]
            lista[k+1]=aux

print("La lista ordenada de menor a mayor es")

for i in range(5):
    print(lista[i])

for i in range(4):
    for k in range(4-i):
        if lista[k]<lista[k+1]:
            aux=lista[k]
            lista[k]=lista[k+1]
            lista[k+1]=aux

print("La lista ordenada de mayor a menor  es")

for i in range(5):
    print(lista[i])