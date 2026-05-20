#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
#en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
#cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de
#puntos a procesar.
cuadrante1=0    
cuadrante2=0    
cuadrante3=0    
cuadrante4=0    

n=int(input(f"Puntos a procesar"))

for j in range(n):
    
    x=int(input(f"Ingrese los puntos del eje x"))
    y=int(input(f"Ingrese los puntos del eje y"))

    if x>0 and y >0:
        cuadrante1= cuadrante1+1
        print(f"Los puntos ingresados en el cuadrante 1 son eje X {x} y en el eje Y {y}")

    else:
        if x<0 and y>0:
            cuadrante2=cuadrante2+1
            print(f"Los puntos ingresados en el cuadrante 2 son eje X {x} y en el eje Y {y}")
        else:
            if x<0 and y<0:
                cuadrante3=cuadrante3+1
                print(f"Los puntos ingresados en el cuadrante 3 son eje X {x} y en el eje Y {y}")
            else:
                cuadrante4=cuadrante4+1
                print(f"Los puntos ingresados en el cuadrante 4 son eje X {x} y en el eje Y {y}")

print(f"Total de puntos en el cuadrante 1 son {cuadrante1}")
print(f"Total de puntos en el cuadrante 2 son {cuadrante2}")
print(f"Total de puntos en el cuadrante 3 son {cuadrante3}")
print(f"Total de puntos en el cuadrante 4 son {cuadrante4}")
