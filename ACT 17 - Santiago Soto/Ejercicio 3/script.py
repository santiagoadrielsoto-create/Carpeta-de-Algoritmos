"""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""

empleados=[]
falto=[]
inasistencias=[]
for i in range(3):
    nombre=input(F"Ingrese el nombre del empleado {i+1}")
    empleados.append(nombre)
    n=int(input(F"Cuantas inasistencias tuvo el empleado {nombre}"))
    inasistencias.append(n)
    faltas=[]
    for i in range(n):
        dias=int(input(f"Que Dias del mes faltaste?"))
        faltas.append(dias)
    falto.append(faltas)
    
for i in range(3):
    print(f"El empleado {empleados[i]} falto los dias {falto[i]}.")
    print(F"Tiene una cantidad de inasistencias de {inasistencias[i]}")
mayor=0
c=0
for i in range(3):
    if inasistencias[i]>mayor:
        mayor=inasistencias[i]
        c=i+1

for i in range(3):
    if inasistencias[i]<mayor:
        print(f"El empleado {empleados[i]} tiene menos faltas que el empleado{c}")

