"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista. 

"""

lista1=[]
lista2=[]
lista3=[]

for i in range(4):
    li1=int(input(f"Ingrese el numero {i+1} de la lista 1"))
    li2=int(input(f"Ingrese el numero {i+1} de la lista 2"))
    lista1.append(li1)
    lista2.append(li2)

for j in range(4):
    suma=0
    suma= lista1[j]+ lista2[j]    

    lista3.append(suma)


print("La tercer lista es")
print(lista3)