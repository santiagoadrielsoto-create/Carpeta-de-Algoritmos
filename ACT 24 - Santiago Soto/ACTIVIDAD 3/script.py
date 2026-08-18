"""3:
 Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
 en cada habitación de la casa.
 Crear un diccionario donde la Clave sea el nombre del ambiente (ej: "Cocina", "Dormitorio")
 y el Valor sea una lista de tuplas, donde cada tupla represente un
 dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
 Desarrollar las siguientes funciones:
 1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
    ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
    operador decida no cargar más para ese ambiente.
 2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
    en Watts acumulado en cada una de ellas.
 3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
    energía consume de toda la casa (el valor máximo individual dentro de todas las
    listas del diccionario), indicando en qué habitación se encuentra.
"""

def cargar():
    hogar = {}

    for i in range(3):
        ambiente = input(f"Ingrese el nombre de la habitacion {i + 1}: ")
        dispositivos = []

        continuar = "si"
        while continuar.lower() == "si":
            nombre_disp = input(
                f"Ingrese el nombre del dispositivo para {ambiente}: "
            )
            consumo = float(
                input(f"Ingrese el consumo en Watts de {nombre_disp}: ")
            )

            dispositivos.append((nombre_disp, consumo))

            continuar = input(
                "¿Desea ingresar otro dispositivo en esta habitacion? (si/no): "
            )

        hogar[ambiente] = dispositivos

    return hogar


def consumo_por_habitacion(hogar):
    print("Consumo por Habitacion")
    for ambiente in hogar:
        dispositivos = hogar[ambiente]
        total_watts = 0

        for i in range(len(dispositivos)):
            disp = dispositivos[i]
            total_watts = total_watts + disp[1]

        print("Habitacion:", ambiente, " Consumo Total:", total_watts, "Watts")


def dispositivo_critico(hogar):
    max_consumo = -1
    disp_critico = ""
    hab_critica = ""

    for ambiente in hogar:
        dispositivos = hogar[ambiente]

        for i in range(len(dispositivos)):
            disp = dispositivos[i]
            nombre = disp[0]
            consumo = disp[1]

            if consumo > max_consumo:
                max_consumo = consumo
                disp_critico = nombre
                hab_critica = ambiente

    if disp_critico != "":
        print(
            "Dispositivo critico:",
            disp_critico,
            "con",
            max_consumo,
            "Watts en la habitacion:",
            hab_critica,
        )


hogar = cargar()
consumo_por_habitacion(hogar)
dispositivo_critico(hogar)
