"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""

def retornar(lista):
    mayores=[]
    for i in range(len(lista)):
        if lista[i]>=18:
            mayores.append(lista[i])
            
    return mayores
    
edades=[1,2,19,18,17,29,30]
mayores=retornar(edades)
print(F"Las edades mayores de edad son {mayores} ")