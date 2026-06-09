"""
4. Elaborar una función que muestre la tabla de multiplicar del valor que le
enviemos como parámetro. Definir un segundo parámetro llamado termino
que por defecto almacene el valor 10. Se deben mostrar tantos términos de
la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con
argumentos nombrados.
"""

def multiplicar(numero, termino=10):
    for i in range(1,termino+1):
        print(F"la multiplicacion {i} es {numero} X {i} = {numero*i}")

print(multiplicar(3,5))
print(multiplicar(1,15))
print(multiplicar(5,20))