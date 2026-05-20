"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""

vendedores=[]
ventas=[]

for i in range(5):
    nombre=input(f"Ingrese el nombre del vendedor {i+1}")
    vendedores.append(nombre)

    venta=int(input(f"Ingrese las ventas de {nombre}"))
    ventas.append(venta)

for i in range(4):
    for j in range(4-i):
        if ventas[j]<ventas[j+1]:
            aux = ventas[j]
            ventas[j]=ventas[j+1]
            ventas[j+1]=aux
            aux2=vendedores[j]
            vendedores[j]=vendedores[j+1]
            vendedores[j+1]=aux2

print(f"La lista de ventas ordenada de mayor a menor.")
for x in range(5):
    print(vendedores[x],ventas[x])
    
    if x==4:
        print(f"El vendedor que menos ventas tuvo fue {vendedores[x]}{ventas[x]}")
