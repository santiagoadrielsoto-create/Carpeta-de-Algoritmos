"""
3-

Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [[&quot;juan&quot;,(2000,3000,4233)] , [&quot;ana&quot;,(3444,1000,5333)] , etc. ]
"""

def carga():
    empleado=[]
    for i in range(5):
        nom=input(F"Ingrese el nombre del empleado {i+1}")
        sueldos=[]
        for x in range(3):
            su=int(input(F"Ingrese el sueldo de {nom} en el mes {x+1}"))
            sueldos.append(su)
        sueldo=tuple(sueldos)
        empleado.append([nom,sueldo])
    return empleado
   
def suma(empleado):
    for i in range(5):
       
        suma=0
        for f in range(3):
            suma=suma +  empleado[i][1][f]
        print(F"La suma total de los ultimos 3 sueldos del empleado {empleado[i][0]} es de {suma}")
       
def mayor(empleado):
     for i in range(5):
       
        suma=0
        for f in range(3):
            suma=suma +  empleado[i][1][f]
        if suma>10000:
            print(F"El empleado {empleado[i][0]} supero el ingreso trimestrl de 10.000 con un total en estos tres meses de {suma}")

empleado=carga()
suma(empleado)
mayor(empleado)