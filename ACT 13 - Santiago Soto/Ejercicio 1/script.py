#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
#empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
#programa deberá informar el importe que gasta la empresa en sueldos al personal.

mas100=0
mas300=0
s=int(input(f"Cuantos empleados tienen en la empresa?"))
total=0
for x in range(s):
    empleados=input(f"Ingrese el nombre del empleado numero {x+1}")
    sueldos=int(input(f"Ingrese el sueldo de {empleados}"))

    total=total+sueldos

    if sueldos>=100 and sueldos<=300:
        print(f"El empleado {empleados} cobra entre 100$ y 300$ con un total de {sueldos}")
        mas100=mas100+1

    else:
        if sueldos>300:
            print(f"El empleado {empleados} cobra mas de 300$ con un total de {sueldos}")
            mas300=mas300+1


print(f"La cantidad de empleados que cobran entre 100$ y 300$ son {mas100}")
print(f"La cantidad de empleados que cobran mas de 300$ son {mas300}")
print(f"El total de gastos que genera la empresa en sueldos de los {s} empleados es de {total}")