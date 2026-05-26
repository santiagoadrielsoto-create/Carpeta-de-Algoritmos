"""
4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""

n=int(input(F"Cuantos empleados tienen en la empresa?"))
empleados=[]
sueldos=[]

for i in range(n):
    nombre=input(F"Ingrese el nombre del empleado {i+1}")
    empleados.append(nombre)
    suel=int(input(F"Ingrese el sueldo del empleado {nombre}"))
    sueldos.append(suel)

filtroN=[]
filtroS=[]
c=0
for i in range(n):
    if sueldos[i]<10000:
        filtroN.append(empleados[i])
        filtroS.append(sueldos[i])
        c=c+1

print("Los empleados que aun siguen son:")
for i in range(c):
    print(F"El empleado {filtroN[i]} con un sueldo de {filtroS[i]}")