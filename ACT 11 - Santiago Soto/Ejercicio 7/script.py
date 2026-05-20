#7. Escribir un programa en el cual: dada una lista de tres valores numéricos
#distintos se calcule e informe su rango de variación (debe mostrar el mayor
#y el menor de ellos)

num1 = int(input("Ingrese el numero 1"))
num2 = int(input("Ingrese el numero 2"))
num3 = int(input("Ingrese el numero 3"))

if num1>num2 and num1>num3:
    print("El numero mayor es " , num1)

else: 
    if num2>num1 and num2>num3:
        print("El numero mayor es " , num2)

    else:
        print("El numero mayor es " , num3)


if num1<num2 and num1<num3:
    print("Y el menor numero es " , num1)

else: 
    if num2<num1 and num2<num3:
        print("Y el menor numero es " , num2)

    else:
        print("Y el menor numero es " , num3)