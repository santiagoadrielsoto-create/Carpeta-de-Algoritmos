#3. Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
#(mensajes &quot;Lista 1 mayor&quot;, &quot;Lista 2 mayor&quot;, &quot;Listas iguales&quot;) Tener en cuenta que
#puede haber dos o más estructuras repetitivas en un algoritmo.

total1=0
total2=0

for j in range(15):
        valores=int(input(f"Ingrese el valor numero {j+1} de la lista 1"))
        total1=total1+valores

for g in range(15):
        valores=int(input(f"Ingrese el valor numero {g+1} de la lista 2"))
        total2=total2+valores

if total1>total2:
        print(f"Los valores ingresados en la lista 1 son los mas grandes con un total de {total1}")
else: 
        if total2>total1:
                  print(f"Los valores ingresados en la lista 2 son los mas grandes con un total de {total2}")

        else:
                  print(f"Los valores ingresados en la lista 1 y en la lista 2 son iguales.")

