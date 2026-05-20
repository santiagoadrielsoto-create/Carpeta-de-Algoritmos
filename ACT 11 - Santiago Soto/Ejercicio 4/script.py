#4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
#mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un
#número entero)

num= int(input("Ingrese un numero del numero 1 al 99"))

if num>0 and num<10:
 print("El numero tiene 1 digito")
 
else :
   if num>9 and num<99:
    print("El numero tiene 2 digitos")
   else:
     print("El numero tiene mas de 2 digitos")