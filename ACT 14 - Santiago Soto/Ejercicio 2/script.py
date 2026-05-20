#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
#empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
#que permita almacenar los sueldos de los empleados agrupados en dos
#listas.

mañana = []
tarde = []

for i in range(4):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1} del turno mañana: "))
    mañana.append(sueldo)

for i in range(4):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1} del turno tarde: "))
    tarde.append(sueldo)

print("Sueldos del turno mañana:", mañana)
print("Sueldos del turno tarde:", tarde)
