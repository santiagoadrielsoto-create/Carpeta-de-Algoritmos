""" CONSIGNA - PUNTO 4:
 Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
 y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
 Diseñar un diccionario donde la Clave sea el identificador único del dron (ej: "DRON-01")
 y el Valor sea una lista de tuplas que almacene las coordenadas de
 las paradas programadas: [(latitud, longitud)].
 Desarrollar las siguientes funciones:
 1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
    uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas geográficas.
 2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
    de coordenadas asociadas.
 3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
    cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad de elementos).
"""

def cargar():
    drones = {}

    for i in range(3):
        id_dron = input(
            f"Ingrese el identificador del dron {i + 1} (ej: DRON-01): "
        )
        cant_paradas = int(
            input(f"¿Cuántas paradas realizará el {id_dron}?: ")
        )
        paradas = []

        for j in range(cant_paradas):
            latitud = float(
                input(f"Ingrese la latitud de la parada {j + 1}: ")
            )
            longitud = float(
                input(f"Ingrese la longitud de la parada {j + 1}: ")
            )
            paradas.append((latitud, longitud))

        drones[id_dron] = paradas

    return drones


def imprimir_rutas(drones):
    print("--- Listado Completo de Rutas ---")
    for id_dron, paradas in drones.items():
        print("Dron:", id_dron)
        for idx, coord in enumerate(paradas):
            print(
                "  Parada",
                idx + 1,
                ": Latitud",
                coord[0],
                ", Longitud",
                coord[1],
            )


def ruta_mas_larga(drones):
    max_paradas = -1
    dron_mas_largo = ""

    for id_dron, paradas in drones.items():
        if len(paradas) > max_paradas:
            max_paradas = len(paradas)
            dron_mas_largo = id_dron

    if dron_mas_largo != "":
        print(
            "El dron con la ruta más larga es",
            dron_mas_largo,
            "con",
            max_paradas,
            "paradas registradas.",
        )


drones = cargar()
imprimir_rutas(drones)
ruta_mas_larga(drones)