#5. Realizar un programa que lea los lados de n triángulos, e informar:
#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
#iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.


equilátero=0
isósceles=0
escaleno=0
n= int(input("Cuantos triangulos vas a ingresar?"))

for j in range(n):
    lado1=int(input(f"Ingrese el lado 1 del triangulo {j+1}"))
    lado2=int(input(f"Ingrese el lado 2 del triangulo {j+1}"))
    lado3=int(input(f"Ingrese el lado 3 del triangulo {j+1}"))
    
    if lado1==lado2 and lado1==lado3:
      print (f"El triangulo {j+1} es equilátero")
      equilátero=equilátero+1
    else:
        if (lado1 == lado2 and lado1 !=lado3) or (lado1 != lado2 and lado1==lado3):
           print(f"El triangulo {j+1} es isósceles")
           isósceles= isósceles+1

        else:
           print(f"El triangulo {j+1} es escaleno")
           escaleno=escaleno+1

print(f"La cantidad de triangulos equiláteros son {equilátero}, la cantidad de isósceles son {isósceles}, y la cantidad de escalenos son {escaleno}.")
