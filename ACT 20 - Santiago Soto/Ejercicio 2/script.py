"""
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""

def carga():
    arti=[]
    pre=[]
    for i in range(5):
        art=input(F"Ingrese el nombre del artuticulo {i+1}")
        pr=int(input(F"Ingrese el precio de este articulo"))
        arti.append(art)
        pre.append(pr)
       
    return arti, pre
def imprimir(arti,pre):
    for i in range(5):
        if i==0:
            print(F"El nombre del 1er articulo es {arti[i]} y su precio es {pre[i]}" )
        elif i==1:
            print(F"El nombre del 2do articulo es {arti[i]} y su precio es {pre[i]} ")
        elif i==2:
            print(F"El nombre del 3er articulo es {arti[i]} y su precio es {pre[i]} " )
        else:
            print(F"El nombre del {i}to articulo es {arti[i]} y su precio es {pre[i]} " )
def mayor(arti,pre):
    mayor=0
    c=0
    for i in range(5):
        if pre[i]>mayor:
            mayor=pre[i]
            c=i
            
    print(F"El mayor precio es el del articulo {arti[c]} con un precio de {mayor}")

def orden(arti,pre):
    importe=int(input(F"Ingrese un importe para organizar los precios y mostrar los que sean meores o iguales a este."))
    
    for i in range(5):
        
        if pre[i] < importe:
            print(F"El articulo {arti[i]} tiene un precio menor al importe con un precio de {pre[i]}.")
        elif pre[i] == importe:
            print(F"El articulo {arti[i]} tiene un precio igual al importe con un precio de {pre[i]}.")
            
arti,pre=carga()
imprimir(arti,pre)
mayor(arti,pre)
orden(arti,pre)