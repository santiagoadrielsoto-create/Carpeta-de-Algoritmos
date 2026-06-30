"""

Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
 Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: &quot;192.168.1.50&quot;) y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos).
"""

def cargar():
    direcciones={}
    for i in range(4):
        ip=input(F"Ingrese la direcciom IP {i+1} sospechosa:")
        lista=[]
        nom=input(F"Ingrese el nobre del dispositivo con ip {ip} : ")
        inte=int(input(F"Ingrese cuantos intentos fallidos tuvo:"))
        lista.append((nom,inte))
        direcciones[ip]=lista
    return direcciones

def Imprimir(direcciones):
    print("Listado completo de los ip sosprchosos:")
    for ip in direcciones:
        print(F"En la direccion ip {ip}" )
        for nom,inte in direcciones[ip]:
           print(F"El nombre de dispositivo es {nom} y tiene una cantidad de {inte} intentos fallidos.")

def bloqueo(direcciones):
    print("Las direcciones IP bloqueadas con mas de 5 intentos fallidos son:")
    for ip in direcciones:
        for nom,inte in direcciones[ip]:
            if inte>5:
                print(F"La IP{ip} fue bloqueada debido a sus mas de 5 intentos fallidos.")
direcciones=cargar()
Imprimir(direcciones)
bloqueo(direcciones) 
