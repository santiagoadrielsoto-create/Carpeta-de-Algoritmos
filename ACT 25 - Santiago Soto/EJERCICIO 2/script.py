"""
2-
Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
cámaras de control.
 Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
Desarrollar las siguientes funciones:
1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
cámaras para armar las tuplas y agregarlas a la lista.
2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
cámaras. Importante: Realizar el recorrido utilizando un bucle for que
desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
utilizar índices numéricos como [0] o [1]).
3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
ubicadas en el hemisferio norte (latitud mayor a cero).
"""

def cargar_cords():
    camaras=[]    
    for i in range(4):
        lat=int(input(F"Ingrese la latitud de la camara {i+1}"))
        lon=int(input(F"Ingrese la longitud de la camara {i+1}"))
        coordenada=(lat,lon)
        camaras.append(coordenada)

    return camaras

def listar(camaras):
    print("Listado de camaras")
    for lat, lon in camaras:
                print(F"la Latitud es {lat} y la longitud es {lon}")
               

def filtro(camaras):

    contador=0
    for lat, lon in camaras:

        if lat>0:
            contador=contador+1
    print(F"La cantidad de camaras en el hemisferio norte son {contador}")


camaras=cargar_cords()
listar(camaras)
filtro(camaras)