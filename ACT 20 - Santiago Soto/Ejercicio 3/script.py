"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def valores(lista):
    
    positivo=[]
    negativo=[]
    
    for i in range(len(lista)):
        if lista[i] >=0:
            positivo.append(lista[i])
            
        else:
            negativo.append(lista[i])
            
    print(F"Numeros positivos de los ingresados {positivo} ")
    print(F"Numeros negativos de los ingresados {negativo} ")
    
numeros=[1,4,5,-9,-20,-31,11,41,0,-1]
valores(numeros)