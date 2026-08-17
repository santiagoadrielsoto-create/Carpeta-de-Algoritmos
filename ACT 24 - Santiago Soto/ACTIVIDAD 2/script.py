""" CONSIGNA - PUNTO 2:
 En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
 para realizar misiones cooperativas.
 Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej: "DragonesDeFuego")
 y el Valor sea una lista de cadenas con los nombres de los jugadores (nicknames) que lo integran.
 Desarrollar las siguientes funciones:
 1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
    preguntar cuántos integrantes posee para cargar sus respectivos nombres de
    usuario en la lista interna.
 2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
    de miembros que posee cada uno.
 3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
    gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
    "Solitario" (no pertenece a ningún clan)."""


def cargar():
    gremios = {}

    for i in range(3):
        nombre_gremio = input(f"Ingrese el nombre del gremio {i + 1}: ")
        cantidad = int(input(f"¿Cuántos integrantes tiene {nombre_gremio}?: "))
        integrantes = []

        for j in range(cantidad):
            nickname = input(f"Ingrese el nickname del jugador {j + 1}: ")
            integrantes.append(nickname)

        gremios[nombre_gremio] = integrantes

    return gremios


def listar_clanes(gremios):
    print("--- Listado de Gremios ---")
    for gremio, integrantes in gremios.items():
        print("Gremio:", gremio, "| Cantidad de miembros:", len(integrantes))


def buscar_jugador(gremios):
    buscado = input("Ingrese el nickname del jugador a buscar: ")
    encontrado = False

    for gremio, integrantes in gremios.items():
        if buscado in integrantes:
            print("El jugador", buscado, "pertenece al gremio:", gremio)
            encontrado = True
            break

    if not encontrado:
        print(
            "El jugador",
            buscado,
            "es Solitario (no pertenece a ningún clan).",
        )


gremios = cargar()
listar_clanes(gremios)
buscar_jugador(gremios)