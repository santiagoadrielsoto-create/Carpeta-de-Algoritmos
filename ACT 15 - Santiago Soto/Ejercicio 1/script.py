"""
1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar &quot;Muy Bueno&quot; si la nota es mayor o
igual a 8, &quot;Bueno&quot; si la nota está entre 4 y 7, y colocar &quot;Insuficiente&quot;
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.
"""

nombre=[]
notas=[]

for i in range (4):
    nom=input(f"Ingrese el nombre del alumno {i+1}")
    nombre.append(nom)
    no=int(input(f"Ingrese la nota del 1 al 10 "))
    notas.append(no)
    print(f"")

bueno=0
for i in range(4):
    
    if notas[i]>=8:
        print(f"Felicidades {nombre[i]} sacaste mas de 8")
        print(f"con un total de {notas[i]} , Nota muy buena")
        bueno=bueno+1

    else:
        if notas[i]>4 and notas[i]<7:
            print(f"El alumno {nombre[i]} tiene aprobado")
            print(f"con un total de {notas[i]}, Nota buena")

        else:
            print(f"En proceso {nombre[i]} ")
            print(f"con un total de {notas[i]} , Nota insuficiente")

print(f"La cantidad de alumno que sacaron mas de 8 fueron un total de {bueno}")