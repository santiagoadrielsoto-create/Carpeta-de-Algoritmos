"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""

def carga():

    valor1=int(input(f"Ingrese el primer valor."))
    valor2=int(input(f"Ingrese el segundo valor."))
    valor3=int(input(f"Ingrese el tercer valor."))
        
    if valor1< valor2 and valor1<valor3:
        print(f"El menor valor es el 1 con {valor1}")

    else:
        if valor2<valor1 and valor2<valor3:
            print(f"El menor valor es el 2 con  {valor2}")

        else:
            print(f"El menor valor es el 3 con  {valor3}")

carga() 
carga()