"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A".
"""

def cantidad(let):

    cant = 0
    
    for i in range(len(let)):
        if let[i] == 'a' or let[i]=="A":
            cant = cant + 1
            
    print(f"La cantidad de 'a' o 'A' que tiene el string: {let} es de {cant}")

def cargar():
    texto = input("Ingrese un string de palabras que pueda contener minusculas y mayusculas: ")
    cantidad(texto)

cargar()