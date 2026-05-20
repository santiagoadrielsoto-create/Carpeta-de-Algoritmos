"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.
"""

n=int(input(f"Cuantos empleados tiene la empresa?"))

sueldos=[]

for i in range(n):
    su=int(input(f"Cuanto cobra el empleado {i+1}"))
    sueldos.append(su)
print("Lista de sueldos sin ordenar")
print(sueldos)


for i in range(n-1):
    for j in range (n-1-i):
        if sueldos[j]>sueldos[j+1]:
            aux=sueldos[j]
            sueldos[j]=sueldos[j+1]
            sueldos[j+1]=aux

print(f"La lista de sueldos ordenada es {sueldos}")