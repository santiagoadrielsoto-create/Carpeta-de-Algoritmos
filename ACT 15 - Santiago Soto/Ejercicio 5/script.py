"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""

pais=[]
habitantes=[]

for i in range(5):
    nombre=input(f"Ingrese el nombre del pais")
    hab=int(input(f"Ingrese cuantos habitantes tiene {nombre}"))

    pais.append(nombre)
    habitantes.append(hab)

for a in range(4):
    for k in range(4 - a):

        if pais[k] > pais[k + 1]:           
            aux = pais[k]
            pais[k] = pais[k + 1]
            pais[k + 1] = aux

            aux2 = habitantes[k]
            habitantes[k] = habitantes[k + 1]
            habitantes[k + 1] = aux2
print("")
print("Paises ordenados en orden alfabetico")
for i in range(5):
    print(pais[i], habitantes[i])

for a in range(4):
    for k in range(4 - a):
        if habitantes[k] < habitantes[k + 1]:
            aux = habitantes[k]
            habitantes[k] = habitantes[k + 1]
            habitantes[k + 1] = aux

            aux2 = pais[k]
            pais[k] = pais[k + 1]
            pais[k + 1] = aux2
print("")
print("Paises ordenados por cantidad de habitantes de mayor a menor")
for i in range(5):
    print(pais[i], habitantes[i])