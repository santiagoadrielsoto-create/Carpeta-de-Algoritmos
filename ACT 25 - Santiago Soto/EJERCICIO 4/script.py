"""
4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
"""


def cargar_inv():
    inventario=[]

    for i in range(5):
        nombre=input(F"Ingrese el nombre del articulo {i+1}")
        precio=float(input(F"Ingrese el precio del articulo"))
        stock=int(input(F"Ingrese el stock actual del articulo"))
        articulo=(nombre,precio,stock)
        inventario.append(articulo)

    return inventario

def imprimir(inventario):
    print("Inventario completo")
    for nombre,precio,stock in inventario:
        print(F"Articulo: {nombre} - Precio: {precio} - Stock: {stock} ")

def valor_inv(inventario):
    total=0
    for nombre,precio,stock in inventario:
        total=total+(precio*stock)
    print(F"El valor total del inventario es de {total}")

def reponer(inventario):
    for nombre,precio,stock in inventario:
        if stock <= 10:
            print(F"Alerta hay que reponer el articulo {nombre}, su stock actual es de {stock}")
inventario=cargar_inv()
imprimir(inventario)
valor_inv(inventario)
reponer(inventario)