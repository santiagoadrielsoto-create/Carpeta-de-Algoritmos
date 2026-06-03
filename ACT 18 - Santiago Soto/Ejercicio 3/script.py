"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""

def calculo(l1,l2,l3,l4):
    superficie=l1*l2
    print(F"La superficie del rectangulo es {superficie} ")
    superficie2=l3*l4
    print(F"La superficie del segundo rectangulo es {superficie2} ")

def mayor(l1,l2,l3,l4):
    superficie1=l1*l2
    superfici2=l3*l4

    print("La mayor superficie.")
    if superficie1>superfici2: 
        print("Es del primer rectangulo")
    else:
        print("Es del segundo rectangulo")

def carga():
    lado1=int(input(F"Ingrese el lado 1 del rectangulo"))
    lado2=int(input(F"ingrese el lado 2 del rectangulo"))

    print("Ingrese los lados del segundo recctangulo")

    lado3=int(input(F"Ingrese el lado 1 del rectangulo"))
    lado4=int(input(F"ingrese el lado 2 del rectangulo"))
    calculo(lado1,lado2,lado3,lado4)
    mayor(lado1,lado2,lado3,lado4)

carga()
