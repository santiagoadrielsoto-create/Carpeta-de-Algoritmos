"""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""
def enteros(n1,n2,n3):
    if n1<n2 and n1<n3:
        print(f"El menor numero es {n1}")
    elif n2<n1 and n2<n3:
        print(f"El menor numero es {n2}")        
    else:
        print(f"El menor numero es {n3}")
    if n1>n2 and n1<n3 or n1<n2 and n1>n3:
        print(F"El numero del medio es {n1}")
    elif n2>n1 and n2<n3 or n2<n1 and n2>n3:
        print(F"El numero del medio es {n2}")
    else:
        print(F"El numero del medio es {n3}")
    if n1>n2 and n1>n3:
        print(F"El mayor numero es {n1}")
    elif n2>n1 and n2>n3:
        print(F"El mayor numero es {n2}")
    else:
        print(F"El mayor numero es {n3}")
        
def cargas():
    num1=int(input(F"Ingrese el primer numero entero"))
    num2=int(input(F"Ingrese el segundo numero entero"))
    num3=int(input(F"Ingrese el tercer numero entero"))
    enteros(num1,num2,num3) 
cargas()