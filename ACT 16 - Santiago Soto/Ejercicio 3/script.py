"""
3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio.
"""

atletas=[]
tiempos=[]


for i in range(6):
    nombre=input(f"Ingrese el nombre del atleta {i+1}")
    atletas.append(nombre)

    tiempo=float(input(f"Ingrese el tiempo de {nombre} en la carrera de 100M"))
    tiempos.append(tiempo)
j=0
k=0
suma=0
mejor=9999999999999999999999999
peor=0
for i in range(5):
    suma=suma+tiempos[i]

    if tiempos[i]<mejor:
        mayor=tiempos[i]
        j=i

    if tiempos[i]>peor:
        menor=tiempos[i]
        k=i

print(f"El atleta con mejor tiempo es {atletas[j]} con un tiempo de {mejor}")
print(f"El atleta con peor tiempo es {atletas[k]} con un tiempo de {peor}")
promedio=suma/5

print(f"El promedio de tiempo es {promedio}")

for i in range(6):
    if tiempos[i]>promedio:
        print(f"El atleta {atletas[i]} no supero el promedio con un tiempo de {tiempos[i]}")

    else:
        print(f"El atleta {atletas[i]} supero el promedio con un tiempo de {tiempos[i]}")