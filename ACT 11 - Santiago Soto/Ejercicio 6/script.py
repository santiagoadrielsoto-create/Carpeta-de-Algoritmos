#6. De un operario se conoce su sueldo y los años de antigüedad. Se pide
#confeccionar un programa que lea los datos de entrada e informe:
#a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10
#años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10
#años, otorgarle un aumento de 5 %.
#c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
#cambios.

años= int(input("Ingrese sus años de antigüedad"))
sueldo= int(input("Ingrese su sueldo"))

if sueldo<500 and años >=10:
    print("su sueldo se aumenta en un 20%")
    pagar= sueldo*1.2
    print("su sueldo a pagar es ", pagar)

else:
    if sueldo<500 and años<10:
         print("su sueldo se aumenta en un 5%")
         pagar= sueldo*1.05
         print("su sueldo a pagar es ", pagar)

    else: 
        print("Su suelde es ", sueldo)