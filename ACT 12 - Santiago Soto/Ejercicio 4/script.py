#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.
total=0
for j in range(10):
    valores=int(input(f"Ingrese el valor numero {j+1}"))
    if valores < 0:
        print(f"El valor ingresado numero {j+1} es negativo")

    else:
         print(f"El valor ingresado numero {j+1} es positivo")
             
    if valores%15 == 0:
        print(f"El valor ingresado numero {j+1} es multiplo de 15")

    if valores%2 == 0:
        total =total + valores

print(f"El total de la suma de los valores que son pares es {total}")