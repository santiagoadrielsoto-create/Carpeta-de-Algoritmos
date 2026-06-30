"""
1-
Crear un diccionario en Python que defina como clave el número de documento de
una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""

def carga():
    documentos={}
    for i in range(4):
        nombre=input(F"Ingrese el nombre de la persona {i+1}:")
        dni=int(input(F"Ingrese el dni de {nombre}:"))
        documentos[dni]=nombre
    return documentos

def imprimir(documentos):
    print("Listado completo de DNI y a quien le corresponde:")
    for dni in documentos:
        print(dni, documentos[dni])

def consultar(documento):
    doc=int(input(F"Ingrese el DNI a consultar"))
    if doc in documentos:
        print(F"El propietario del DNI {doc} es {documentos[doc]}")
documentos=carga()
imprimir(documentos)
consultar(documentos)