"""Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4."""

def cargar():
    sala = [
        [1,0,0,0,1],
        [0,1,0,1,1],
        [0,0,0,0,0],
        [1,1,1,0,0],
        [1,0,0,0,1]
    ]

    cantidad = int(input("¿Cuántas entradas quiere sacar? "))
    fila = int(input("¿En qué fila? (1 al 5): ")) - 1

    datos = [sala, fila, cantidad]

    return datos


def reservar_consecutivos(datos):

    sala = datos[0]
    fila = datos[1]
    cantidad = datos[2]

    contador = 0

    for i in range(len(sala[fila])):

        if sala[fila][i] == 0:
            contador = contador + 1
        else:
            contador = 0

        if contador == cantidad:

            inicio = i - cantidad + 1

            for j in range(inicio, i + 1):
                sala[fila][j] = 1
                respuesta=[sala]
            print("Reserva realizada.")
            print("Las columnas asignadas son:")

            for j in range(inicio, i + 1):
                print("Columna", j)

            print("Estado de la sala:")
            for f in respuesta[0]:
                print(f)
                
            return

    print("No fue posible realizar la reserva.")


datos = cargar()
reservar_consecutivos(datos)

