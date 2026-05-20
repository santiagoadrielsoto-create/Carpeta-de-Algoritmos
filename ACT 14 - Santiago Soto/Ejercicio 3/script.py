#4. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
#si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o
#más posiciones en la lista)

lista=[]
mayor = 0

for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    lista.append(numero)

for numero in lista:
    if numero > mayor:
        mayor = numero
        print(f"El número mayor hasta ahora es: {mayor}")

    else:
        if numero == mayor:
            print(f"El número {numero} se repite en la lista.")




