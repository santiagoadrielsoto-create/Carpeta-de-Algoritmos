#5. Cargar por teclado y almacenar en una lista las alturas de 5 personas
#(valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más
#altas que el promedio y cuántas más bajas.

alturas=[]
suma=0
promedio=0
for i in range(5):
    centimetro= int(input(f"Ingrese la altura de la persona {i+1}"))
    alturas.append(centimetro)
    suma=suma+centimetro


promedio=suma/5
print(f"El promedio de altura es {suma/5}.")

for i in range(5):
    if alturas[i] >=promedio:
        print(f"La persona {i+1} supera al promedio con una altura de {alturas[i]}")