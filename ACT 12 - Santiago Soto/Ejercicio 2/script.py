#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
#altura promedio de las personas.
n= int(input(f"Cuantas personas vas a ingresar?"))
total=0

for f in range(n):

    conjunto = int(input(f"Ingrese el total de altura de  la persona {f+1}"))
    total = total + conjunto

print(f"El promedio de altura de las {n} personas de de {total/n}")



