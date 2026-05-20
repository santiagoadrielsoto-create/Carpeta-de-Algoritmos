#3. Realizar un programa que solicite la carga por teclado de dos números, si el
#primero es mayor al segundo informar su suma y diferencia, en caso
#contrario informar el producto y la división del primero respecto al segundo.

num1= int(input("Ingrese el valor del numero 1"))
num2= int(input("Ingrese el valor del numero 2"))

if num1>num2:
 suma = num1+num2
 diferencia = num1-num2
 print("La suma del num1 + num2 es de " , suma , " y su diferencia es de " , diferencia)
else:
  multiplicacion= num2*num1
  division = num2/num1
  print("La multiplicacion entre el num2 y el num1 es de ", multiplicacion , " y su division es " , division)

  