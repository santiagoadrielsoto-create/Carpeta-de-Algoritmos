"""3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto."""

def suma(a1,a2,a3=0,a4=0,a5=0):
    sumas=a1+a2+a3+a4+a5
    return sumas


sumas=print(suma(1,2))
sumas=print(suma(1,2,3))
sumas=print(suma(1,2,3,4))
sumas=print(suma(1,2,3,4,5))
