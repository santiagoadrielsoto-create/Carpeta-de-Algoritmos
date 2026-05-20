"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""

estudiantes= []

nota=[]

for i in range(6):
    nombre=input(f"Ingrese el nombre del estudiante {i+1}")
    estudiantes.append(nombre)

    notas=float(input(f"Ingrese la nota de {nombre}"))
    nota.append(notas)
mayor=0
menor=9999999999999999999999999999999999999999999999999999999999999999


for i in range(6):
    if nota[i] > mayor:
        mayor=nota[i]  
        


    if nota[i] < menor:
        menor=nota[i]  
        
Nmayor=[]
Nmenor=[]

for i in range(6):
    if nota[i] == mayor:
        Nmayor.append(estudiantes[i])

    if nota[i] == menor:   
        Nmenor.append(estudiantes[i])
     

if len(Nmayor) == 1:
    print(f"El Estudiante con mayor nota es {Nmayor} con una nota de {mayor}")

else:
    print(f"Los estudiantes con la mayor nota de {mayor} son")
    for i in range(len(Nmayor)):
        print(f"{Nmayor[i]}")

if len(Nmenor) == 1:
    print(f"El Estudiante con menor nota es {Nmenor} con una nota de {menor}")

else:
    print(f"Los estudiantes con la menor nota de {menor} son")
    for i in range(len(Nmenor)):
        print(f"{Nmenor[i]}")