"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def empl():
    sueld=[]
    for i in range(10):
        a=int(input(F"Ingrese el sueldo del empleado numero {i+1}"))
        sueld.append(a)
    
    for i in range(10):
        print(F"El sueldo del empleado {i+1} es de {sueld[i]}")
    
    return sueld

def mayor(sueld):
    mayor=0
    for i in range(10):
        if sueld[i]>4000:
            mayor=mayor+1
    print(F"la cantidad de ")
    
def promedio(sueld):

    suma=0
    for i in range(10):
        suma=suma + sueld[i]


    promedio=suma/10
    print(F"El promedio es de {promedio}")
    return promedio 
    
def menor(sueld,promedio):
    
    for i in range(10):
        if sueld[i]<promedio:
            print(F"El ingreso de la persona {i+1} no supera el promedio con un sueldo de {sueld[i]}")

    

sueld=empl()
mayor(sueld)
promedio=promedio(sueld)
menor(sueld,promedio)