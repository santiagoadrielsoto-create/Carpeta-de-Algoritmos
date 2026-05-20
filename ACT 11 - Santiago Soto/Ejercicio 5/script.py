#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
#el número es positivo, negativo o nulo (es decir cero)

num= int(input("Ingrese el numero que desee"))
if num> 0:
    print("El numero ingresado es positivo")

else :
    if num<0:
        print("El numero ingresado es negativo")

    else:
        print("El numero ingresado es nulo")    