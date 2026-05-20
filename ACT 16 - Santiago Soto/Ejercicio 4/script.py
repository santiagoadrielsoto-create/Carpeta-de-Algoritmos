"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""

docentes=[]
puntajes=[]


for i in range(6):
    nombre=input(f"Ingrese el nombre del docente {i+1}")
    docentes.append(nombre)

    notas=float(input(f"Ingrese el puntaje de {nombre} del 1 al 10"))
    puntajes.append(notas)

mayor=0
menor=9999999999999999999999999999999999999999999999999999999999999999
j=0
k=0
for i in range(6):
    if puntajes[i] > mayor:
        mayor=puntajes[i]  
        j=i


    if puntajes[i] < menor:
        menor=puntajes[i]  
        k=i

print(f"El docente con la nota mas alta es {docentes[j]} con una nota de {mayor}")
print(f"El docente con la nota mas baja es {docentes[k]} con una nota de {menor}")

for i in range(5):
    for x in range(5-i):
        if puntajes[x]<puntajes[x+1]:
            aux=puntajes[x]
            puntajes[x]=puntajes[x+1]
            puntajes[x+1]=aux
            aux2=docentes[x]
            docentes[x]=docentes[x+1]
            docentes[x+1]=aux2

print(f"Lista ordenada de mayor a menor de los docentes y si aprobaron o no")

for i in range(6):
    if puntajes[i]>=6:
        print(f"El docente {docentes[i]} aprobo con una nota de {puntajes[i]} ¡Felicidades!")

    else:
        print(f"El docente {docentes[i]} desaprobo con una nota de {puntajes[i]} . A seguir intentando!!")