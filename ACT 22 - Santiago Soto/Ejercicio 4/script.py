"""
4-
Un observatorio astronómico registra los descubrimientos de nuevos planetas
fuera del sistema solar.
 Diseñar un diccionario donde la Clave sea el nombre científico del
exoplaneta (ej: &quot;Kepler-22b&quot;) y el Valor sea una tupla con sus datos:
(distancia_anios_luz, tipo_de_atmosfera, es_habitable_booleano).
Desarrollar las siguientes funciones:
1. Cargar catálogo: Registrar por teclado la información de 4 exoplanetas
descubiertos.
2. Buscar exoplaneta: Permitir al usuario ingresar el nombre de un
exoplaneta por teclado. Si el exoplaneta se encuentra en el diccionario
(utilizando el operador in), mostrar todos sus detalles físicos y si reúne
condiciones de habitabilidad. De lo contrario, mostrar un cartel indicando:
&quot;El exoplaneta no figura en el catálogo actual&quot;.
3. Reportar Habitables: Mostrar en pantalla únicamente los nombres de los
exoplanetas cargados que fueron marcados como habitables.
"""
def cargar():
    exoplanetas={}
    for i in range(4):
        pla=input(F"Ingrese el nombre del exoplaneta descubierto numero {i+1}:")
        lista=[]
        dist=int(input(F"Ingrese la distancia de años luz que tiene el exoplaneta:"))
        atm=input(F"Ingrese el tipo de atmosfera que tiene el exoplaneta:")
        habi=input(F"El planeta es habitable? [si/no]")
        lista.append((dist,atm,habi))
        exoplanetas[pla]=lista
    return exoplanetas

def buscar(exoplanetas):
    print("Planetas que figuran en el catalogo")
    for pla in exoplanetas:
        for dist,atm,habi in exoplanetas[pla]:
            if habi== "si":
                print(F"El exoplaneta {pla} es habitable, su atmosfera es {atm} y se encuentra a unos {dist} años luz.")
            else:
                print("El exoplaneta no figura en el catálogo actual")

def habitables(exoplanetas):
    print("Los exoplanetas habitables son:")
    for pla in exoplanetas:
        for dist,atm,habi in exoplanetas[pla]:
            if habi== "si":
                print(F"El exoplaneta {pla} fue encontrado habitable.")
           
exoplanetas=cargar()
buscar(exoplanetas)
habitables(exoplanetas)