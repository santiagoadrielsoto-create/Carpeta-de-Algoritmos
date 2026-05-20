#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
#informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
mayor=0
menor=0
for f in range(10):
    indice=f
    notas=int(input(f"Ingrese la nota del alumno   {indice+1} "))

    if notas> 7 and notas<=10:
         print(f"La nota del alumno {indice+1} es mayor a 7 con un total de {notas}" )
         mayor = mayor+ 1
    
    else:
         if notas==7:
            
              print (f"La nota del alumno {indice+1}   es igual a 7")
              mayor= mayor + 1

         else :
              print (f"La nota del alumno {indice+1} es menor a 7 con un total de  {notas}")
              menor= menor+ 1


print(f"cantidad de alumno con nota mayor o igual a 7 son {mayor}")
print(f"cantidad de alumno con nota menor a 7 son {menor}")

