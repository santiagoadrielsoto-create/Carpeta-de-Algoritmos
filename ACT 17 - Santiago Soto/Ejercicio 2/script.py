"""
2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor.
"""

paises=[]
temperaturas=[]

for i in range(4):
    nombre=input(f"Ingrese el nombre del pais {i+1}")
    paises.append(nombre)
    aux_T=[]
    for j in range(3):
        temps=float(input(f"Ingrese la temperatura en promedio del mes {j+1} en {nombre}"))
        aux_T.append(temps)
    temperaturas.append(aux_T)
sumas=[]
for i in range(4):
    print(f"En el pais de {paises[i]} la temperatura es de")
    suma=0
    
    for x in range(3):
        suma=suma+temperaturas[i][x]
        print(f"La temperatura del mes {x+1} es de {temperaturas[i][x]}")
    print(f"La temperatura promedio los ultimos 3 meses en {paises[i]} es de {suma/3}")
    sumas.append(suma)

mayor=0
k=0
for i in range(4):
        if sumas[i]>mayor:
            mayor=sumas[i]  
            k=i

print(f"El Pais con mayor temperatura media trimestral es {paises[k]}")